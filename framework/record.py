"""Activity and result records for MetalShift workflows."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class RecordResult(Enum):
    """Supported workflow result states."""

    SUCCESS = "SUCCESS"
    ERROR = "ERROR"
    FATAL = "FATAL"
    NEW = "NEW"


class TestType(Enum):
    """Record classification for reporting."""

    __test__ = False

    TEST_RUN = "TESTRUN"
    TEST_SET = "TESTSET"
    TEST = "TEST"


@dataclass
class Record:
    """Track one test, testset, or test run."""

    name: str
    test_type: TestType
    record_id: Optional[str] = None
    result: RecordResult = RecordResult.NEW
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    activity_table: Dict[str, str] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def log_info(self, message: str, *args: object) -> None:
        formatted = message % args if args else message
        self.activity_table["INFO_%d" % len(self.activity_table)] = formatted

    def log_error(self, message: str, *args: object) -> None:
        formatted = message % args if args else message
        self.result = RecordResult.ERROR
        self.activity_table["ERROR_%d" % len(self.activity_table)] = formatted
        self.errors.append(formatted)

    def log_fatal(self, message: str, *args: object) -> None:
        formatted = message % args if args else message
        self.result = RecordResult.FATAL
        self.activity_table["FATAL_%d" % len(self.activity_table)] = formatted
        self.errors.append(formatted)
        raise RuntimeError(formatted)

    def log_result(self, message: str = "") -> RecordResult:
        self.end_time = datetime.now()
        if self.result == RecordResult.NEW:
            self.result = RecordResult.SUCCESS
        duration = (self.end_time - self.start_time).total_seconds()
        if message:
            final_message = "%s - Duration: %.2fs" % (message, duration)
        else:
            final_message = "Duration: %.2fs" % duration
        self.activity_table["RESULT_%d" % len(self.activity_table)] = final_message
        return self.result
