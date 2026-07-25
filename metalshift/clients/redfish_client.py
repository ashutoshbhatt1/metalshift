"""Redfish-style BMC session and power-state boundary."""

from metalshift.contracts import BMCSessionResult, PowerResult


class RedfishClient:
    """Simulate Redfish sessions and host power actions."""

    def __init__(self) -> None:
        self.sessions: dict[str, str] = {}
        self.power_states: dict[str, str] = {}

    def create_session(self, host_name: str, username: str) -> BMCSessionResult:
        token = "redfish-session-%s" % host_name
        self.sessions[host_name] = token
        return {"host": host_name, "username": username, "session": token}

    def set_power_state(self, host_name: str, state: str) -> PowerResult:
        self.power_states[host_name] = state
        return {"host": host_name, "power_state": state}

    def get_power_state(self, host_name: str) -> str:
        return self.power_states.get(host_name, "Off")
