
# inject invalid firmware commands
# simulate malformed unauthorized and empty command inputs


# inject malformed command
def inject_malformed_command(firmware):
    return firmware.send_command("@@@")


# inject empty command
def inject_empty_command(firmware):
    return firmware.send_command("")


# inject unauthorized command
def inject_unauthorized_command(firmware):
    return firmware.send_command("ERASE_FLASH")