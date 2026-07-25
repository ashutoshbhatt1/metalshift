"""Atomic volume operations."""

from framework.test_base import TestBase
from metalshift.clients.api_client import APIClient
from metalshift.contracts import VolumeResult


class VolumeTests(TestBase):
    def create_attached_volume(
        self,
        api_client: APIClient,
        name: str,
        size_gb: int,
        host_id: str,
    ) -> VolumeResult:
        self.info("Creating volume %s", name)
        return api_client.create_volume(name, size_gb, host_id)
