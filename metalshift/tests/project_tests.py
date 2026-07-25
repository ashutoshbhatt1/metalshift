"""Atomic project operations."""

from framework.test_base import TestBase
from metalshift.clients.api_client import APIClient
from metalshift.contracts import ProjectResult


class ProjectTests(TestBase):
    def create_project(self, api_client: APIClient, name: str) -> ProjectResult:
        self.info("Creating project %s", name)
        project = api_client.create_project(name)
        self.info("Created project %s", project["id"])
        return project
