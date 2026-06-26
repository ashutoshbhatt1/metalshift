"""Atomic project operations."""

from typing import Dict

from framework.test_base import TestBase


class ProjectTests(TestBase):
    def create_project(self, api_client, name: str) -> Dict[str, str]:
        self.info("Creating project %s", name)
        project = api_client.create_project(name)
        self.info("Created project %s", project["id"])
        return project
