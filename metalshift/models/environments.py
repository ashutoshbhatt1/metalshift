"""Sample vendor-neutral environments for local pytest execution."""

from typing import List

from .base import Credentials, EnvironmentConfig, HostSpec, LifecycleData, NetworkSpec, VolumeSpec


def _data(name: str, host_count: int, timeout_seconds: int) -> LifecycleData:
    hosts = [
        HostSpec(name="%s-node-%d" % (name, idx), image="ubuntu-22.04", interfaces=["eth0", "eth1"])
        for idx in range(1, host_count + 1)
    ]
    return LifecycleData(
        environment=EnvironmentConfig(
            name=name,
            api_url="https://api.%s.example.invalid" % name,
            bmc_url="https://bmc.%s.example.invalid" % name,
            network_controller_url="https://network.%s.example.invalid" % name,
            datacenter="%s-dc" % name,
            timeout_seconds=timeout_seconds,
        ),
        credentials=Credentials(username="automation-user", token_env_var="METALSHIFT_SAMPLE_TOKEN"),
        project_name="%s-lifecycle-project" % name,
        hosts=hosts,
        volumes=[
            VolumeSpec(name="%s-volume-1" % name, size_gb=100, attach_to_host=hosts[0].name),
        ],
        networks=[
            NetworkSpec(
                name="%s-tenant-net" % name,
                vlan_id=120,
                cidr="192.0.2.0/24",
                gateway="192.0.2.1",
                interfaces=["eth0", "eth1"],
                bond_name="bond0",
                bond_mode="lacp",
                switch_ports=["leaf1:1/1", "leaf2:1/1"],
            )
        ],
    )


def lab_a_data() -> LifecycleData:
    return _data("lab_a", host_count=2, timeout_seconds=1800)


def staging_data() -> LifecycleData:
    return _data("staging", host_count=3, timeout_seconds=2700)


def smoke_data() -> LifecycleData:
    return _data("smoke", host_count=1, timeout_seconds=900)


def all_environment_data() -> List[LifecycleData]:
    return [lab_a_data(), staging_data(), smoke_data()]
