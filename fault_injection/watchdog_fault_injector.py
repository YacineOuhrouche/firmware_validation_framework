
# inject watchdog related failures
# simulate watchdog timeout and disabled watchdog behavior


# inject watchdog timeout
def inject_watchdog_timeout(firmware):
    return firmware.trigger_watchdog_timeout()


# inject disabled watchdog condition
def inject_disabled_watchdog(firmware):
    firmware.watchdog_enabled = False
    return firmware.trigger_watchdog_timeout()