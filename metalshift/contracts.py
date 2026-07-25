"""Typed result contracts shared across clients and orchestration layers."""

from typing import TypedDict


class ProjectResult(TypedDict):
    id: str
    name: str
    state: str


class HostResult(TypedDict):
    id: str
    name: str
    project_id: str
    state: str


class VolumeResult(TypedDict):
    id: str
    name: str
    size_gb: int
    host_id: str
    state: str


class BMCSessionResult(TypedDict):
    host: str
    username: str
    session: str


class PowerResult(TypedDict):
    host: str
    power_state: str


class BondResult(TypedDict):
    name: str
    mode: str
    interfaces: list[str]


class VlanResult(TypedDict):
    network: str
    vlan_id: int
    ports: list[str]


class LeaseResult(TypedDict):
    network: str
    host: str
    address: str


class ConnectivityResult(TypedDict):
    host: str
    target: str
    reachable: bool


class NetworkValidationResult(TypedDict):
    ports: dict[str, str]
    bond: BondResult
    vlan: VlanResult
    lease: LeaseResult
    connectivity: ConnectivityResult


class LifecycleResult(TypedDict):
    project: ProjectResult
    hosts: list[HostResult]
    bmc_sessions: list[BMCSessionResult]
    networks: list[NetworkValidationResult]
    power: list[PowerResult]
    volumes: list[VolumeResult]
