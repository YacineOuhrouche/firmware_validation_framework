
# validate firmware diagnostics utilities
# verify log parsing failure classification and crash analysis


from adapters.fake_firmware_adapter import FakeFirmwareAdapter
from diagnostics.log_parser import count_logs
from diagnostics.log_parser import find_logs
from diagnostics.log_parser import detect_error_logs
from diagnostics.failure_classifier import classify_failure
from diagnostics.failure_classifier import classify_severity
from diagnostics.crash_analyzer import analyze_failure
from diagnostics.crash_analyzer import is_critical_failure


# verify log counter returns number of logs
def test_count_logs_returns_log_count():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("START")

    result = count_logs(firmware.get_logs())

    assert result == 2


# verify log search finds matching logs
def test_find_logs_returns_matching_entries():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("START")

    result = find_logs(firmware.get_logs(), "start")

    assert result == ["start command accepted"]


# verify error log detector finds invalid command logs
def test_detect_error_logs_finds_invalid_command_log():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("BAD_COMMAND")

    result = detect_error_logs(firmware.get_logs())

    assert "invalid command rejected" in result


# verify invalid command failure classification
def test_invalid_command_is_classified_as_command_failure():
    result = classify_failure("INVALID_COMMAND")

    assert result == "command_failure"


# verify memory failure severity is critical
def test_memory_failure_severity_is_critical():
    result = classify_severity("STACK_OVERFLOW")

    assert result == "critical"


# verify crash analyzer summarizes failure
def test_crash_analyzer_returns_failure_summary():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.corrupt_memory()

    result = analyze_failure(firmware.get_last_error(), firmware.get_logs())

    assert result["error_code"] == "STACK_OVERFLOW"
    assert result["failure_type"] == "memory_failure"
    assert result["severity"] == "critical"


# verify critical failure detector identifies stack overflow
def test_critical_failure_detector_identifies_stack_overflow():
    result = is_critical_failure("STACK_OVERFLOW")

    assert result is True