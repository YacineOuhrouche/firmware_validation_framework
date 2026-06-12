# validate firmware command processing
# verify valid invalid malformed and unauthorized commands

from adapters.fake_firmware_adapter import FakeFirmwareAdapter


# verify firmware boots into idle state
def test_firmware_boots_to_idle():
    firmware = FakeFirmwareAdapter()

    result = firmware.boot()

    assert result == "OK"
    assert firmware.get_state() == "IDLE"


# verify start command transitions to running
def test_start_command_moves_to_running():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    result = firmware.send_command("START")

    assert result == "OK"
    assert firmware.get_state() == "RUNNING"


# verify stop command transitions to idle
def test_stop_command_moves_to_idle():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("START")

    result = firmware.send_command("STOP")

    assert result == "OK"
    assert firmware.get_state() == "IDLE"


# verify invalid command is rejected
def test_invalid_command_does_not_crash_firmware():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    result = firmware.send_command("BAD_COMMAND")

    assert result == "ERROR"
    assert firmware.get_state() == "IDLE"
    assert firmware.get_last_error() == "INVALID_COMMAND"