from __future__ import annotations

import bz2
import logging
import os

import requests

from vunnel import utils
from vunnel.utils.oval_parser import Config, parse


class Parser:
    _url_mappings_ = [  # noqa: RUF012
        # Legacy data for RHEL:5 - no longer available from endpoint after 1st July, 2023; however, it is available in the
        # preload archive.
        {
            "base_url": "https://www.redhat.com/security/data/oval",
            "manifest_path": "PULP_MANIFEST",
            "oval_paths": ["com.redhat.rhsa-all.xml.bz2"],
            "skip_download": True,
        },
        {
            "base_url": "https://www.redhat.com/security/data/oval/v2",
            "manifest_path": "PULP_MANIFEST",
            "oval_paths": [
                "RHEL6/rhel-6.oval.xml.bz2",
                "RHEL7/rhel-7.oval.xml.bz2",
                "RHEL8/rhel-8.oval.xml.bz2",
                "RHEL9/rhel-9.oval.xml.bz2",
            ],
        },
    ]

    def __init__(self, workspace, config: Config, logger=None, download_timeout=125):
        self.config = config
        self.download_timeout = download_timeout
        self.workspace = workspace

        if not logger:
            logger = logging.getLogger(self.__class__.__name__)

        self.logger = logger
        self._urls = set()

    @property
    def urls(self) -> list[str]:
        return list(self._urls)

    def _get_workspace_xml_filepath(self, oval_url_path: str) -> str:
        return os.path.join(self.workspace.input_path, oval_url_path.rstrip(".bz2"))

    @utils.retry_with_backoff()
    def _download_oval_file(self, base_url: str, oval_url_path: str):
        xml_file_path = self._get_workspace_xml_filepath(oval_url_path=oval_url_path)
        try:
            oval_url = f"{base_url}/{oval_url_path}"
            self.logger.info(f"begin downloading OVAL file from {oval_url}")
            r = requests.get(oval_url, stream=True, timeout=self.download_timeout)
            if r.status_code == 200:
                # ensure any nested directories get created
                os.makedirs(os.path.dirname(xml_file_path), exist_ok=True)
                with open(xml_file_path, "wb") as extracted:
                    decompressor = bz2.BZ2Decompressor()
                    for chunk in r.iter_content(chunk_size=1024):
                        uncchunk = decompressor.decompress(chunk)
                        extracted.write(uncchunk)

                self.logger.info(f"finish downloading OVAL file from {oval_url}")
            else:  # noqa: RET505
                raise Exception(f"GET {oval_url} failed with HTTP error {r.status_code}")
        except Exception:
            self.logger.exception("error downloading OVAL file")
            raise Exception("error downloading OVAL file")  # noqa: B904

    @utils.retry_with_backoff()
    def _download(self):
        for m in self._url_mappings_:
            base_url = m["base_url"]
            manifest_path = m["manifest_path"]
            oval_paths = m["oval_paths"]
            skip_download = m.get("skip_download", False)
            self._urls.add(f"{base_url}/{manifest_path}")

            for p in oval_paths:
                self._urls.add(f"{base_url}/{p}")
                if not skip_download:
                    self._download_oval_file(base_url, p)

    def xml_paths(self):
        paths = []
        for m in self._url_mappings_:
            oval_paths = m["oval_paths"]
            skip_download = m.get("skip_download", False)

            for p in oval_paths:
                # normalize and return results
                file_path = self._get_workspace_xml_filepath(p)
                if skip_download and not os.path.exists(file_path):
                    self.logger.warning(f"skip processing OVAL file {p}")
                    continue
                paths.append(file_path)
        return paths

    def parse(self):
        vuln_dict = {}

        for file_path in self.xml_paths():
            self.logger.info(f"begin parsing OVAL file {file_path}")
            partial_results = parse(file_path, self.config, vuln_dict=vuln_dict)
            vuln_dict.update(partial_results)
            self.logger.info(f"finish parsing OVAL file {file_path}")

        return vuln_dict

    def get(self):
        self._download()
        return self.parse()
