
# inject sensor faults into firmware
# simulate invalid low high and stuck sensor values


# inject low out of range sensor value
def inject_low_sensor_fault(firmware):
    firmware.set_sensor_value(-100.0)
    return firmware.process_sensor()


# inject high out of range sensor value
def inject_high_sensor_fault(firmware):
    firmware.set_sensor_value(300.0)
    return firmware.process_sensor()


# inject stuck sensor value
def inject_stuck_sensor_fault(firmware):
    firmware.set_sensor_value(25.0)
    return firmware.read_sensor()