
# validate firmware report generation
# verify report content status and output file creation


import json

from automation.report_generator import create_report
from automation.report_generator import save_report


# verify report is marked pass when no failures exist
def test_report_status_is_pass_when_no_failures():
    report = create_report(
        total_tests=36,
        passed_tests=36,
        failed_tests=0,
    )

    assert report["status"] == "PASS"


# verify report is marked fail when failures exist
def test_report_status_is_fail_when_failures_exist():
    report = create_report(
        total_tests=36,
        passed_tests=35,
        failed_tests=1,
    )

    assert report["status"] == "FAIL"


# verify report file is created
def test_report_file_is_created(tmp_path):
    report = create_report(
        total_tests=36,
        passed_tests=36,
        failed_tests=0,
    )

    output_path = tmp_path / "report.json"
    result = save_report(report, output_path)

    assert result == str(output_path)
    assert output_path.exists()


# verify saved report contains expected fields
def test_saved_report_contains_expected_fields(tmp_path):
    report = create_report(
        total_tests=36,
        passed_tests=36,
        failed_tests=0,
    )

    output_path = tmp_path / "report.json"
    save_report(report, output_path)

    with output_path.open("r", encoding="utf-8") as file:
        saved_report = json.load(file)

    assert saved_report["total_tests"] == 36
    assert saved_report["passed_tests"] == 36
    assert saved_report["failed_tests"] == 0
    assert saved_report["status"] == "PASS"