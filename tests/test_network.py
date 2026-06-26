import pytest


@pytest.mark.network
def test_network_client_configures_lacp_vlan_and_ip_pool(network_client, lab_environment):
    network = lab_environment.networks[0]

    ports = network_client.configure_physical_ports(network.switch_ports, state="trunk")
    bond = network_client.configure_lacp_bond(network.bond_name, network.interfaces)
    vlan = network_client.assign_vlan(network.name, network.vlan_id, network.switch_ports)
    lease = network_client.allocate_ip(network.name, host_name=lab_environment.hosts[0].name)

    assert ports["leaf1:1/1"] == "trunk"
    assert bond["mode"] == "lacp"
    assert vlan["vlan_id"] == 120
    assert lease["address"] == "192.0.2.10"


@pytest.mark.network
def test_network_client_validates_connectivity(network_client, lab_environment):
    network = lab_environment.networks[0]
    network_client.assign_vlan(network.name, network.vlan_id, network.switch_ports)
    result = network_client.validate_connectivity(lab_environment.hosts[0].name, network.gateway)

    assert result["reachable"] is True
    assert result["target"] == "192.0.2.1"
