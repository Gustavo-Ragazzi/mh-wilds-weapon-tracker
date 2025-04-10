import sys
import os


def get_config_path():
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, "weapons_config.json")
