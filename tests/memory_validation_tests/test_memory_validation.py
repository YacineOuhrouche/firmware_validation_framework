
# validate firmware memory protection
# verify stack heap overflow and safe state behavior


from adapters.fake_firmware_adapter import FakeFirmwareAdapter


# verify normal memory usage passes validation
def test_normal_memory_usage_passes_validation():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    result = firmware.check_memory()

    assert result == "OK"
    assert firmware.is_safe_state() is False


# verify stack overflow is detected
def test_stack_overflow_is_detected():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    firmware.memory_usage["stack_used"] = 2000
    result = firmware.check_memory()

    assert result == "ERROR"
    assert firmware.get_last_error() == "STACK_OVERFLOW"
    assert firmware.get_state() == "SAFE"
    assert firmware.is_safe_state() is True


# verify heap overflow is detected
def test_heap_overflow_is_detected():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    firmware.memory_usage["heap_used"] = 3000
    result = firmware.check_memory()

    assert result == "ERROR"
    assert firmware.get_last_error() == "HEAP_OVERFLOW"
    assert firmware.get_state() == "SAFE"
    assert firmware.is_safe_state() is True


# verify memory corruption forces safe state
def test_memory_corruption_forces_safe_state():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    firmware.corrupt_memory()

    assert firmware.get_last_error() == "STACK_OVERFLOW"
    assert firmware.get_state() == "SAFE"
    assert firmware.is_safe_state() is True


# verify memory corruption creates log entry
def test_memory_corruption_creates_log_entry():
    firmware = FakeFirmwareAdapter()
    firmware.boot()

    firmware.corrupt_memory()

    assert "memory corruption detected" in firmware.get_logs()