"""In-memory infrastructure API boundary used by local tests."""

from typing import Dict


class APIClient:
    """Simulate project, host, and volume APIs without real infrastructure."""

    def __init__(self):
        self.projects: Dict[str, Dict[str, str]] = {}
        self.hosts: Dict[str, Dict[str, str]] = {}
        self.volumes: Dict[str, Dict[str, object]] = {}

    def create_project(self, name: str) -> Dict[str, str]:
        project = {"id": "project-%d" % (len(self.projects) + 1), "name": name, "state": "active"}
        self.projects[project["id"]] = project
        return project

    def delete_project(self, project_id: str) -> Dict[str, str]:
        project = self.projects.pop(project_id)
        return dict(project, state="deleted")

    def create_host(self, name: str, project_id: str) -> Dict[str, str]:
        host = {
            "id": "host-%d" % (len(self.hosts) + 1),
            "name": name,
            "project_id": project_id,
            "state": "ready",
        }
        self.hosts[host["id"]] = host
        return host

    def create_volume(self, name: str, size_gb: int, host_id: str) -> Dict[str, object]:
        volume = {
            "id": "volume-%d" % (len(self.volumes) + 1),
            "name": name,
            "size_gb": size_gb,
            "host_id": host_id,
            "state": "attached",
        }
        self.volumes[volume["id"]] = volume
        return volume
