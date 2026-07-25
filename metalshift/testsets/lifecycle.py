"""Lifecycle testset orchestration."""

from framework.record import Record
from metalshift.clients.api_client import APIClient
from metalshift.clients.network_client import NetworkClient
from metalshift.clients.redfish_client import RedfishClient
from metalshift.contracts import LifecycleResult
from metalshift.models.base import LifecycleData
from metalshift.tests.host_tests import HostTests
from metalshift.tests.network_tests import NetworkTests
from metalshift.tests.project_tests import ProjectTests
from metalshift.tests.volume_tests import VolumeTests


class LifecycleTestSet:
    """Compose server, storage, BMC, and network operations into one workflow."""

    def __init__(
        self,
        record: Record,
        api_client: APIClient,
        redfish_client: RedfishClient,
        network_client: NetworkClient,
        data: LifecycleData,
    ) -> None:
        self.record = record
        self.api_client = api_client
        self.redfish_client = redfish_client
        self.network_client = network_client
        self.data = data
        self.projects = ProjectTests(record)
        self.hosts = HostTests(record)
        self.volumes = VolumeTests(record)
        self.networks = NetworkTests(record)

    def run(self) -> LifecycleResult:
        project = self.projects.create_project(self.api_client, self.data.project_name)
        hosts = [self.hosts.create_host(self.api_client, host.name, project["id"]) for host in self.data.hosts]
        bmc_sessions = [self.hosts.create_bmc_session(self.redfish_client, host.name) for host in self.data.hosts]
        networks = [
            self.networks.configure_network(self.network_client, network, self.data.hosts[0].name)
            for network in self.data.networks
        ]
        power = [
            self.hosts.set_bmc_power(self.redfish_client, host.name, host.desired_power_state)
            for host in self.data.hosts
        ]
        volumes = [
            self.volumes.create_attached_volume(self.api_client, volume.name, volume.size_gb, hosts[0]["id"])
            for volume in self.data.volumes
        ]
        self.record.log_result("Lifecycle workflow complete")
        return {
            "project": project,
            "hosts": hosts,
            "bmc_sessions": bmc_sessions,
            "networks": networks,
            "power": power,
            "volumes": volumes,
        }
