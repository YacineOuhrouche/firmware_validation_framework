
# validate firmware sensor processing
# verify normal sensor values limits and safe state behavior


from adapters.fake_firmware_adapter import FakeFirmwareAdapter


# verify normal sensor value is processed successfully
def test_normal_sensor_value_is_processed():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.set_sensor_value(25.0)

    result = firmware.process_sensor()

    assert result == "OK"
    assert firmware.get_state() == "IDLE"
    assert firmware.is_safe_state() is False


# verify low out of range sensor value is rejected
def test_low_out_of_range_sensor_value_enters_safe_state():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.set_sensor_value(-100.0)

    result = firmware.process_sensor()

    assert result == "ERROR"
    assert firmware.get_state() == "SAFE"
    assert firmware.is_safe_state() is True
    assert firmware.get_last_error() == "SENSOR_OUT_OF_RANGE"


# verify high out of range sensor value is rejected
def test_high_out_of_range_sensor_value_enters_safe_state():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.set_sensor_value(200.0)

    result = firmware.process_sensor()

    assert result == "ERROR"
    assert firmware.get_state() == "SAFE"
    assert firmware.is_safe_state() is True
    assert firmware.get_last_error() == "SENSOR_OUT_OF_RANGE"


# verify valid sensor processing creates log entry
def test_sensor_processing_adds_log_entry():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.set_sensor_value(30.0)

    firmware.process_sensor()

    assert "sensor processed" in firmware.get_logs()


# verify invalid sensor processing creates error log entry
def test_invalid_sensor_processing_adds_error_log_entry():
    firmware = FakeFirmwareAdapter()
    firmware.boot()
    firmware.set_sensor_value(300.0)

    firmware.process_sensor()

    assert "sensor out of range" in firmware.get_logs()