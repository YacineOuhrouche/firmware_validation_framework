
# load yaml configuration files
# provide reusable config loading for validation modules


import yaml


# load yaml file from path
def load_config(path):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)