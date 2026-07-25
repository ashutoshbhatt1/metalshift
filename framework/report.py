"""JSON report aggregation for MetalShift workflows."""

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from .record import Record, RecordResult, TestType


@dataclass
class Report:
    """Aggregate records and write report artifacts."""

    name: str
    start_time: datetime = field(default_factory=datetime.now)
    records: List[Record] = field(default_factory=list)
    output_dir: Path = field(default_factory=lambda: Path("reports"))

    def new_test_record(self, name: str, test_type: TestType) -> Record:
        record = Record(name=name, test_type=test_type, record_id="rec_%d" % len(self.records))
        self.records.append(record)
        return record

    def generate_summary(self) -> Dict[str, object]:
        total = len(self.records)
        success = sum(1 for record in self.records if record.result == RecordResult.SUCCESS)
        error = sum(1 for record in self.records if record.result == RecordResult.ERROR)
        fatal = sum(1 for record in self.records if record.result == RecordResult.FATAL)
        return {
            "total": total,
            "success": success,
            "error": error,
            "fatal": fatal,
            "pass_rate": "%.2f%%" % (success / total * 100) if total else "0%",
        }

    def save_json(self, filename: Optional[str] = None) -> Path:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        target = self.output_dir / (filename or "report_%s.json" % datetime.now().strftime("%Y%m%d_%H%M%S"))
        payload = {
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "summary": self.generate_summary(),
            "records": [
                {
                    "name": record.name,
                    "test_type": record.test_type.value,
                    "result": record.result.value,
                    "start_time": record.start_time.isoformat(),
                    "end_time": record.end_time.isoformat() if record.end_time else None,
                    "activities": record.activity_table,
                    "errors": record.errors,
                }
                for record in self.records
            ],
        }
        target.write_text(json.dumps(payload, indent=2))
        return target
