
# analyze firmware log output
# extract events errors and reset messages


# count log entries
def count_logs(logs):
    return len(logs)


# find logs containing keyword
def find_logs(logs, keyword):
    return [log for log in logs if keyword in log]


# detect error logs
def detect_error_logs(logs):
    error_keywords = ["invalid", "error", "out of range", "corruption"]

    return [
        log for log in logs
        if any(keyword in log for keyword in error_keywords)
    ]