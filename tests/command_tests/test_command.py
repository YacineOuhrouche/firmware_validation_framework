# validate firmware command processing
# verify valid invalid malformed and unauthorized commands

from adapters.fake_firmware_adapter import FakeFirmwareAdapter


# verify valid start command is accepted
def test_valid_start_command_is_accepted():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    result = firmware.send_command("START")

    assert result == "OK"
    assert firmware.get_state() == "RUNNING"


# verify valid stop command is accepted
def test_valid_stop_command_is_accepted():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("START")

    result = firmware.send_command("STOP")

    assert result == "OK"
    assert firmware.get_state() == "IDLE"


# verify reset command returns firmware to boot state
def test_reset_command_returns_to_boot():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.send_command("START")

    result = firmware.send_command("RESET")

    assert result == "OK"
    assert firmware.get_state() == "BOOT"


# verify malformed command is rejected
def test_malformed_command_is_rejected():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    result = firmware.send_command("@@@")

    assert result == "ERROR"
    assert firmware.get_last_error() == "INVALID_COMMAND"


# verify empty command is rejected
def test_empty_command_is_rejected():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    result = firmware.send_command("")

    assert result == "ERROR"
    assert firmware.get_last_error() == "INVALID_COMMAND"


# verify unauthorized command does not change state
def test_unauthorized_command_does_not_change_state():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    result = firmware.send_command("ERASE_FLASH")

    assert result == "ERROR"
    assert firmware.get_state() == "IDLE"
    assert firmware.get_last_error() == "INVALID_COMMAND"