from framework.record import RecordResult, TestType
from framework.report import Report


def test_report_writes_json_summary(tmp_path):
    report = Report(name="MetalShift Test Report", output_dir=tmp_path)
    record = report.new_test_record("network-lifecycle", TestType.TEST_SET)
    record.log_info("configured LACP bond")
    record.log_result("workflow complete")

    path = report.save_json("summary.json")
    content = path.read_text()

    assert path.name == "summary.json"
    assert '"success": 1' in content
    assert "configured LACP bond" in content


def test_record_tracks_recoverable_error():
    report = Report(name="MetalShift Test Report")
    record = report.new_test_record("host-power", TestType.TEST)

    record.log_error("host did not reach expected state")
    result = record.log_result()

    assert result == RecordResult.ERROR
    assert record.errors == ["host did not reach expected state"]
