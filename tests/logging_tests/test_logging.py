
# validate firmware logging behavior
# verify event logs error logs and recovery logs


from adapters.fake_firmware_adapter import FakeFirmwareAdapter


# verify boot creates log entry
def test_boot_creates_log_entry():
    firmware = FakeFirmwareAdapter()

    firmware.boot()

    assert "firmware booted" in firmware.get_logs()


# verify start command creates log entry
def test_start_command_creates_log_entry():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    firmware.send_command("START")

    assert "start command accepted" in firmware.get_logs()


# verify stop command creates log entry
def test_stop_command_creates_log_entry():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("START")

    firmware.send_command("STOP")

    assert "stop command accepted" in firmware.get_logs()


# verify invalid command creates error log entry
def test_invalid_command_creates_error_log_entry():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    firmware.send_command("BAD_COMMAND")

    assert "invalid command rejected" in firmware.get_logs()


# verify watchdog reset creates log entry
def test_watchdog_reset_creates_log_entry():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    firmware.trigger_watchdog_timeout()

    assert "watchdog reset occurred" in firmware.get_logs()