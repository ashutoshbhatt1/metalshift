"""Vendor-neutral data models for bare-metal lifecycle automation."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class EnvironmentConfig:
    name: str
    api_url: str
    bmc_url: str
    network_controller_url: str
    datacenter: str
    timeout_seconds: int


@dataclass(frozen=True)
class Credentials:
    username: str
    token_env_var: str


@dataclass(frozen=True)
class HostSpec:
    name: str
    image: str
    interfaces: List[str]
    desired_power_state: str = "On"


@dataclass(frozen=True)
class VolumeSpec:
    name: str
    size_gb: int
    attach_to_host: str


@dataclass(frozen=True)
class NetworkSpec:
    name: str
    vlan_id: int
    cidr: str
    gateway: str
    interfaces: List[str]
    bond_name: str
    bond_mode: str
    switch_ports: List[str]


@dataclass(frozen=True)
class LifecycleData:
    environment: EnvironmentConfig
    credentials: Credentials
    project_name: str
    hosts: List[HostSpec]
    volumes: List[VolumeSpec]
    networks: List[NetworkSpec]
