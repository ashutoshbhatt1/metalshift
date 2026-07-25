"""Sample auth client for public-safe login examples."""


class AuthClient:
    """Represent an API login flow using an environment-token reference."""

    def __init__(self) -> None:
        self.session_token: str | None = None

    def login(self, username: str, token_env_var: str) -> dict[str, str]:
        self.session_token = "sample-session-for-%s" % username
        return {"username": username, "token_env_var": token_env_var, "status": "authenticated"}

    def logout(self) -> dict[str, str]:
        self.session_token = None
        return {"status": "logged_out"}
