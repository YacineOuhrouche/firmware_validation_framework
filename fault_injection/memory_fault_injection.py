
# inject memory related failures
# simulate stack overflow heap overflow and memory corruption


# inject stack overflow condition
def inject_stack_overflow(firmware):
    firmware.memory_usage["stack_used"] = firmware.memory_usage["stack_limit"] + 1
    return firmware.check_memory()


# inject heap overflow condition
def inject_heap_overflow(firmware):
    firmware.memory_usage["heap_used"] = firmware.memory_usage["heap_limit"] + 1
    return firmware.check_memory()


# inject generic memory corruption
def inject_memory_corruption(firmware):
    firmware.corrupt_memory()
    return firmware.get_last_error()