class FakeFirmwareAdapter:
    # initialize fake firmware
    def __init__(self):
        self.state = "BOOT"
        self.logs = []
        self.sensor_value = 25.0
        self.memory_usage = {
            "stack_used": 128,
            "stack_limit": 1024,
            "heap_used": 256,
            "heap_limit": 2048,
        }
        self.watchdog_enabled = True
        self.safe_state = False
        self.last_error = None

    # boot firmware into idle state
    def boot(self):
        self.state = "IDLE"
        self.logs.append("firmware booted")
        return "OK"

    # return current firmware state
    def get_state(self):
        return self.state

    # process incoming command
    def send_command(self, command):
        if command == "START":
            self.state = "RUNNING"
            self.logs.append("start command accepted")
            return "OK"

        if command == "STOP":
            self.state = "IDLE"
            self.logs.append("stop command accepted")
            return "OK"

        if command == "RESET":
            self.state = "BOOT"
            self.logs.append("reset command accepted")
            return "OK"

        self.last_error = "INVALID_COMMAND"
        self.logs.append("invalid command rejected")
        return "ERROR"

    # return current sensor value
    def read_sensor(self):
        return self.sensor_value

    # update simulated sensor value
    def set_sensor_value(self, value):
        self.sensor_value = value

    # validate sensor data
    def process_sensor(self):
        if self.sensor_value < -40 or self.sensor_value > 125:
            self.last_error = "SENSOR_OUT_OF_RANGE"
            self.safe_state = True
            self.state = "SAFE"
            self.logs.append("sensor out of range")
            return "ERROR"

        self.logs.append("sensor processed")
        return "OK"

    # return firmware logs
    def get_logs(self):
        return self.logs

    # return memory statistics
    def get_memory_usage(self):
        return self.memory_usage

    # simulate memory corruption
    def corrupt_memory(self):
        self.memory_usage["stack_used"] = 2000
        self.last_error = "STACK_OVERFLOW"
        self.safe_state = True
        self.state = "SAFE"
        self.logs.append("memory corruption detected")

    # validate memory usage
    def check_memory(self):
        if self.memory_usage["stack_used"] > self.memory_usage["stack_limit"]:
            self.last_error = "STACK_OVERFLOW"
            self.safe_state = True
            self.state = "SAFE"
            return "ERROR"

        if self.memory_usage["heap_used"] > self.memory_usage["heap_limit"]:
            self.last_error = "HEAP_OVERFLOW"
            self.safe_state = True
            self.state = "SAFE"
            return "ERROR"

        return "OK"

    # simulate watchdog timeout
    def trigger_watchdog_timeout(self):
        if self.watchdog_enabled:
            self.state = "BOOT"
            self.logs.append("watchdog reset occurred")
            return "RESET"

        return "NO_RESET"

    # return safe state status
    def is_safe_state(self):
        return self.safe_state

    # return last firmware error
    def get_last_error(self):
        return self.last_error