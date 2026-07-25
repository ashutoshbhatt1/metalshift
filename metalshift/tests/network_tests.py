"""Atomic network operations."""

from framework.test_base import TestBase
from metalshift.clients.network_client import NetworkClient
from metalshift.contracts import NetworkValidationResult
from metalshift.models.base import NetworkSpec


class NetworkTests(TestBase):
    def configure_network(
        self,
        network_client: NetworkClient,
        network: NetworkSpec,
        host_name: str,
    ) -> NetworkValidationResult:
        self.info("Configuring network %s", network.name)
        ports = network_client.configure_physical_ports(network.switch_ports, state="trunk")
        bond = network_client.configure_lacp_bond(network.bond_name, network.interfaces)
        vlan = network_client.assign_vlan(network.name, network.vlan_id, network.switch_ports)
        lease = network_client.allocate_ip(network.name, host_name)
        connectivity = network_client.validate_connectivity(host_name, network.gateway)
        return {"ports": ports, "bond": bond, "vlan": vlan, "lease": lease, "connectivity": connectivity}
