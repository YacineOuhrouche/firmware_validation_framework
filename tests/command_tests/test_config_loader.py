
# validate firmware config loading
# verify command and state configuration files load correctly


from src.utils.config_loader import load_config


# verify states config loads valid states
def test_states_config_loads_valid_states():
    config = load_config("configs/states.yaml")

    assert "BOOT" in config["valid_states"]
    assert "IDLE" in config["valid_states"]
    assert "RUNNING" in config["valid_states"]
    assert "SAFE" in config["valid_states"]


# verify commands config loads valid commands
def test_commands_config_loads_valid_commands():
    config = load_config("configs/commands.yaml")

    assert "START" in config["valid_commands"]
    assert "STOP" in config["valid_commands"]
    assert "RESET" in config["valid_commands"]


# verify commands config loads invalid commands
def test_commands_config_loads_invalid_commands():
    config = load_config("configs/commands.yaml")

    assert "BAD_COMMAND" in config["invalid_commands"]
    assert "@@@" in config["invalid_commands"]
    assert "ERASE_FLASH" in config["invalid_commands"]