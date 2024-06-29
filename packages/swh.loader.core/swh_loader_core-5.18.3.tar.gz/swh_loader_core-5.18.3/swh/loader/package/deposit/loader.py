# Copyright (C) 2019-2024  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import datetime
from datetime import timezone
import json
import logging
from typing import Any, Dict, Iterator, List, Mapping, Optional, Sequence, Tuple, Union

import attr
import requests
import sentry_sdk

from swh.core.config import load_from_envvar
from swh.loader.core.loader import DEFAULT_CONFIG
from swh.loader.core.utils import cached_method, download
from swh.loader.package.loader import (
    BasePackageInfo,
    PackageLoader,
    RawExtrinsicMetadataCore,
)
from swh.model.hashutil import hash_to_bytes, hash_to_hex
from swh.model.model import (
    MetadataAuthority,
    MetadataAuthorityType,
    MetadataFetcher,
    ObjectType,
    Person,
    Release,
    Sha1Git,
    TimestampWithTimezone,
)
from swh.storage.algos.snapshot import snapshot_get_all_branches
from swh.storage.interface import StorageInterface

logger = logging.getLogger(__name__)


def now() -> datetime.datetime:
    return datetime.datetime.now(tz=timezone.utc)


@attr.s
class DepositPackageInfo(BasePackageInfo):
    filename = attr.ib(type=str)  # instead of Optional[str]

    author_date = attr.ib(type=datetime.datetime)
    """codemeta:dateCreated if any, deposit completed_date otherwise"""
    commit_date = attr.ib(type=datetime.datetime)
    """codemeta:datePublished if any, deposit completed_date otherwise"""
    client = attr.ib(type=str)
    id = attr.ib(type=int)
    """Internal ID of the deposit in the deposit DB"""
    collection = attr.ib(type=str)
    """The collection in the deposit; see SWORD specification."""
    author = attr.ib(type=Person)
    committer = attr.ib(type=Person)
    release_notes = attr.ib(type=Optional[str])

    @classmethod
    def from_metadata(
        cls, metadata: Dict[str, Any], url: str, filename: str, version: str
    ) -> "DepositPackageInfo":
        # Note:
        # `date` and `committer_date` are always transmitted by the deposit read api
        # which computes itself the values. The loader needs to use those to create the
        # release.

        raw_metadata: str = metadata["raw_metadata"]
        depo = metadata["deposit"]
        return cls(
            url=url,
            filename=filename,
            version=version,
            author_date=depo["author_date"],
            commit_date=depo["committer_date"],
            client=depo["client"],
            id=depo["id"],
            collection=depo["collection"],
            author=parse_author(depo["author"]),
            committer=parse_author(depo["committer"]),
            release_notes=depo["release_notes"],
            directory_extrinsic_metadata=[
                RawExtrinsicMetadataCore(
                    discovery_date=now(),
                    metadata=raw_metadata.encode(),
                    format="sword-v2-atom-codemeta-v2",
                )
            ],
        )

    def extid(self) -> None:
        # For now, we don't try to deduplicate deposits. There is little point anyway,
        # as it only happens when the exact same tarball was deposited twice.
        return None


class DepositLoader(PackageLoader[DepositPackageInfo]):
    """Load a deposited artifact into swh archive."""

    visit_type = "deposit"

    def __init__(
        self,
        storage: StorageInterface,
        url: str,
        deposit_id: str,
        deposit_client: "ApiClient",
        default_filename: str = "archive.tar",
        **kwargs: Any,
    ):
        """Constructor

        Args:
            url: Origin url to associate the artifacts/metadata to
            deposit_id: Deposit identity
            deposit_client: Deposit api client

        """
        super().__init__(storage=storage, url=url, **kwargs)

        self.deposit_id = deposit_id
        self.client = deposit_client
        self.default_filename = default_filename

    @classmethod
    def from_configfile(cls, **kwargs: Any):
        """Instantiate a loader from the configuration loaded from the
        SWH_CONFIG_FILENAME envvar, with potential extra keyword arguments if their
        value is not None.

        Args:
            kwargs: kwargs passed to the loader instantiation

        """
        config = dict(load_from_envvar(DEFAULT_CONFIG))
        config.update({k: v for k, v in kwargs.items() if v is not None})
        deposit_client = ApiClient(**config.pop("deposit"))
        return cls.from_config(deposit_client=deposit_client, **config)

    def get_versions(self) -> Sequence[str]:
        # only 1 branch 'HEAD' with no alias since we only have 1 snapshot
        # branch
        return ["HEAD"]

    def get_metadata_authority(self) -> MetadataAuthority:
        provider = self.metadata()["provider"]
        assert provider["provider_type"] == MetadataAuthorityType.DEPOSIT_CLIENT.value
        return MetadataAuthority(
            type=MetadataAuthorityType.DEPOSIT_CLIENT,
            url=provider["provider_url"],
            metadata={
                "name": provider["provider_name"],
                **(provider["metadata"] or {}),
            },
        )

    def get_metadata_fetcher(self) -> MetadataFetcher:
        tool = self.metadata()["tool"]
        return MetadataFetcher(
            name=tool["name"],
            version=tool["version"],
            metadata=tool["configuration"],
        )

    def get_package_info(
        self, version: str
    ) -> Iterator[Tuple[str, DepositPackageInfo]]:
        p_info = DepositPackageInfo.from_metadata(
            self.metadata(),
            url=self.origin.url,
            filename=self.default_filename,
            version=version,
        )
        yield "HEAD", p_info

    def download_package(
        self, p_info: DepositPackageInfo, tmpdir: str
    ) -> List[Tuple[str, Mapping]]:
        """Override to allow use of the dedicated deposit client"""
        return [self.client.archive_get(self.deposit_id, tmpdir, p_info.filename)]

    def build_release(
        self,
        p_info: DepositPackageInfo,
        uncompressed_path: str,
        directory: Sha1Git,
    ) -> Optional[Release]:
        message = (
            f"{p_info.client}: Deposit {p_info.id} in collection {p_info.collection}"
        )

        if p_info.release_notes:
            message += "\n\n" + p_info.release_notes

        if not message.endswith("\n"):
            message += "\n"

        return Release(
            name=p_info.version.encode(),
            message=message.encode(),
            author=p_info.author,
            date=TimestampWithTimezone.from_dict(p_info.author_date),
            target=directory,
            target_type=ObjectType.DIRECTORY,
            synthetic=True,
        )

    def get_extrinsic_origin_metadata(self) -> List[RawExtrinsicMetadataCore]:
        metadata = self.metadata()
        raw_metadata: str = metadata["raw_metadata"]
        origin_metadata = json.dumps(
            {
                "metadata": [raw_metadata],
                "provider": metadata["provider"],
                "tool": metadata["tool"],
            }
        ).encode()
        return [
            RawExtrinsicMetadataCore(
                discovery_date=now(),
                metadata=raw_metadata.encode(),
                format="sword-v2-atom-codemeta-v2",
            ),
            RawExtrinsicMetadataCore(
                discovery_date=now(),
                metadata=origin_metadata,
                format="original-artifacts-json",
            ),
        ]

    @cached_method
    def metadata(self):
        """Returns metadata from the deposit server"""
        return self.client.metadata_get(self.deposit_id)

    def load(self) -> Dict:
        # First making sure the deposit is known on the deposit's RPC server
        # prior to trigger a loading
        try:
            self.metadata()
        except ValueError:
            logger.exception(f"Unknown deposit {self.deposit_id}")
            sentry_sdk.capture_exception()
            return {"status": "failed"}

        # Then usual loading
        return super().load()

    def finalize_visit(
        self, status_visit: str, errors: Optional[List[str]] = None, **kwargs
    ) -> Dict[str, Any]:
        r = super().finalize_visit(status_visit=status_visit, **kwargs)
        success = status_visit == "full"

        # Update deposit status
        try:
            if not success:
                self.client.status_update(
                    self.deposit_id,
                    status="failed",
                    errors=errors,
                )
                return r

            snapshot_id = hash_to_bytes(r["snapshot_id"])
            snapshot = snapshot_get_all_branches(self.storage, snapshot_id)
            if not snapshot:
                return r
            branches = snapshot.branches
            logger.debug("branches: %s", branches)
            if not branches:
                return r
            rel_id = branches[b"HEAD"].target

            release = self.storage.release_get([rel_id])[0]
            if not release:
                return r

            # update the deposit's status to success with its
            # release-id and directory-id
            self.client.status_update(
                self.deposit_id,
                status="done",
                release_id=hash_to_hex(rel_id),
                directory_id=hash_to_hex(release.target),
                snapshot_id=r["snapshot_id"],
                origin_url=self.origin.url,
            )
        except Exception:
            logger.exception("Problem when trying to update the deposit's status")
            sentry_sdk.capture_exception()
            return {"status": "failed"}
        return r


def parse_author(author) -> Person:
    """See prior fixme"""
    return Person(
        fullname=author["fullname"].encode("utf-8"),
        name=author["name"].encode("utf-8"),
        email=author["email"].encode("utf-8"),
    )


class ApiClient:
    """Private Deposit Api client"""

    def __init__(self, url, auth: Optional[Mapping[str, str]]):
        self.base_url = url.rstrip("/")
        self.auth = None if not auth else (auth["username"], auth["password"])

    def do(self, method: str, url: str, *args, **kwargs):
        """Internal method to deal with requests, possibly with basic http
           authentication.

        Args:
            method (str): supported http methods as in get/post/put

        Returns:
            The request's execution output

        """
        method_fn = getattr(requests, method)
        if self.auth:
            kwargs["auth"] = self.auth
        return method_fn(url, *args, **kwargs)

    def archive_get(
        self, deposit_id: Union[int, str], tmpdir: str, filename: str
    ) -> Tuple[str, Dict]:
        """Retrieve deposit's archive artifact locally"""
        url = f"{self.base_url}/{deposit_id}/raw/"
        return download(url, dest=tmpdir, filename=filename, auth=self.auth)

    def metadata_url(self, deposit_id: Union[int, str]) -> str:
        return f"{self.base_url}/{deposit_id}/meta/"

    def metadata_get(self, deposit_id: Union[int, str]) -> Dict[str, Any]:
        """Retrieve deposit's metadata artifact as json"""
        url = self.metadata_url(deposit_id)
        r = self.do("get", url)
        if r.ok:
            return r.json()

        msg = f"Problem when retrieving deposit metadata at {url}"
        raise ValueError(msg)

    def status_update(
        self,
        deposit_id: Union[int, str],
        status: str,
        errors: Optional[List[str]] = None,
        release_id: Optional[str] = None,
        directory_id: Optional[str] = None,
        snapshot_id: Optional[str] = None,
        origin_url: Optional[str] = None,
    ):
        """Update deposit's information including status, and persistent
        identifiers result of the loading.

        """
        url = f"{self.base_url}/{deposit_id}/update/"
        payload: Dict[str, Any] = {"status": status}
        if release_id:
            payload["release_id"] = release_id
        if directory_id:
            payload["directory_id"] = directory_id
        if snapshot_id:
            payload["snapshot_id"] = snapshot_id
        if origin_url:
            payload["origin_url"] = origin_url
        if errors:
            payload["status_detail"] = {"loading": errors}

        self.do("put", url, json=payload)
