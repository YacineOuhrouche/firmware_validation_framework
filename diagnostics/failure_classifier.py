
# classify firmware failures
# group failures by category and severity


# classify failure type
def classify_failure(error_code):
    if error_code == "INVALID_COMMAND":
        return "command_failure"

    if error_code == "SENSOR_OUT_OF_RANGE":
        return "sensor_failure"

    if error_code == "STACK_OVERFLOW":
        return "memory_failure"

    if error_code == "HEAP_OVERFLOW":
        return "memory_failure"

    if error_code is None:
        return "no_failure"

    return "unknown_failure"


# classify failure severity
def classify_severity(error_code):
    if error_code in ["STACK_OVERFLOW", "HEAP_OVERFLOW"]:
        return "critical"

    if error_code == "SENSOR_OUT_OF_RANGE":
        return "high"

    if error_code == "INVALID_COMMAND":
        return "medium"

    if error_code is None:
        return "none"

    return "unknown"