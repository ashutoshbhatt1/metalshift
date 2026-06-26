"""Atomic volume operations."""

from typing import Dict

from framework.test_base import TestBase


class VolumeTests(TestBase):
    def create_attached_volume(self, api_client, name: str, size_gb: int, host_id: str) -> Dict[str, object]:
        self.info("Creating volume %s", name)
        return api_client.create_volume(name, size_gb, host_id)
