"""Shared base class for atomic operation wrappers."""

from .record import Record


class TestBase:
    """Expose a small logging facade to atomic operations."""

    def __init__(self, record: Record):
        self.record = record

    def info(self, message: str, *args: object) -> None:
        self.record.log_info(message, *args)

    def error(self, message: str, *args: object) -> None:
        self.record.log_error(message, *args)
