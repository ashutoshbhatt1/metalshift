import pytest


@pytest.mark.smoke
def test_environment_names_are_vendor_neutral(all_environment_names):
    assert all_environment_names == ["lab_a", "staging", "smoke"]


@pytest.mark.smoke
def test_lab_environment_contains_server_and_network_data(lab_environment):
    assert lab_environment.environment.name == "lab_a"
    assert lab_environment.hosts[0].interfaces[0] == "eth0"
    assert lab_environment.networks[0].bond_mode == "lacp"
