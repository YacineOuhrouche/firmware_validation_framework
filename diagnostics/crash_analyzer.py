
# analyze firmware crashes
# identify probable crash causes from error codes and logs


from diagnostics.failure_classifier import classify_failure
from diagnostics.failure_classifier import classify_severity


# analyze firmware failure state
def analyze_failure(error_code, logs):
    return {
        "error_code": error_code,
        "failure_type": classify_failure(error_code),
        "severity": classify_severity(error_code),
        "log_count": len(logs),
    }


# determine whether firmware entered critical failure
def is_critical_failure(error_code):
    return classify_severity(error_code) == "critical"