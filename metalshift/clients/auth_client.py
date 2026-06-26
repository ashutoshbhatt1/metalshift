"""Sample auth client for public-safe login examples."""

from typing import Dict, Optional


class AuthClient:
    """Represent an API login flow using an environment-token reference."""

    def __init__(self):
        self.session_token: Optional[str] = None

    def login(self, username: str, token_env_var: str) -> Dict[str, str]:
        self.session_token = "sample-session-for-%s" % username
        return {"username": username, "token_env_var": token_env_var, "status": "authenticated"}

    def logout(self) -> Dict[str, str]:
        self.session_token = None
        return {"status": "logged_out"}
