
# validate watchdog behavior
# verify timeout reset and recovery procedures


from adapters.fake_firmware_adapter import FakeFirmwareAdapter


# verify watchdog timeout resets firmware
def test_watchdog_timeout_resets_firmware():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("START")

    result = firmware.trigger_watchdog_timeout()

    assert result == "RESET"
    assert firmware.get_state() == "BOOT"


# verify watchdog reset creates log entry
def test_watchdog_reset_creates_log_entry():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    firmware.trigger_watchdog_timeout()

    assert "watchdog reset occurred" in firmware.get_logs()


# verify watchdog disabled does not reset firmware
def test_disabled_watchdog_does_not_reset_firmware():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.watchdog_enabled = False

    result = firmware.trigger_watchdog_timeout()

    assert result == "NO_RESET"
    assert firmware.get_state() == "IDLE"


# verify watchdog reset after running mode
def test_watchdog_reset_from_running_mode():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("START")

    firmware.trigger_watchdog_timeout()

    assert firmware.get_state() == "BOOT"