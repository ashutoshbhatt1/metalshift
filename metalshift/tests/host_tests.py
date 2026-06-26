"""Atomic host and BMC operations."""

from typing import Dict

from framework.test_base import TestBase


class HostTests(TestBase):
    def create_host(self, api_client, name: str, project_id: str) -> Dict[str, str]:
        self.info("Creating host %s", name)
        return api_client.create_host(name, project_id)

    def create_bmc_session(self, redfish_client, host_name: str) -> Dict[str, str]:
        self.info("Creating Redfish-style BMC session for %s", host_name)
        return redfish_client.create_session(host_name, username="automation-user")

    def set_bmc_power(self, redfish_client, host_name: str, state: str) -> Dict[str, str]:
        if host_name not in redfish_client.sessions:
            self.create_bmc_session(redfish_client, host_name)
        return redfish_client.set_power_state(host_name, state)
