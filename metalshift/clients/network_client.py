"""Network-controller boundary for bare-metal provisioning tests."""

from metalshift.contracts import (
    BondResult,
    ConnectivityResult,
    LeaseResult,
    VlanResult,
)


class NetworkClient:
    """Simulate physical ports, LACP bonds, VLANs, IP pools, and reachability."""

    def __init__(self) -> None:
        self.ports: dict[str, str] = {}
        self.bonds: dict[str, BondResult] = {}
        self.vlans: dict[str, VlanResult] = {}
        self.leases: dict[str, LeaseResult] = {}

    def configure_physical_ports(self, switch_ports: list[str], state: str) -> dict[str, str]:
        for port in switch_ports:
            self.ports[port] = state
        return {port: self.ports[port] for port in switch_ports}

    def configure_lacp_bond(self, bond_name: str, interfaces: list[str]) -> BondResult:
        bond: BondResult = {"name": bond_name, "mode": "lacp", "interfaces": interfaces}
        self.bonds[bond_name] = bond
        return bond

    def assign_vlan(
        self,
        network_name: str,
        vlan_id: int,
        switch_ports: list[str],
    ) -> VlanResult:
        vlan: VlanResult = {
            "network": network_name,
            "vlan_id": vlan_id,
            "ports": switch_ports,
        }
        self.vlans[network_name] = vlan
        return vlan

    def allocate_ip(self, network_name: str, host_name: str) -> LeaseResult:
        lease: LeaseResult = {
            "network": network_name,
            "host": host_name,
            "address": "192.0.2.10",
        }
        self.leases[host_name] = lease
        return lease

    def validate_connectivity(self, host_name: str, target: str) -> ConnectivityResult:
        return {"host": host_name, "target": target, "reachable": True}
