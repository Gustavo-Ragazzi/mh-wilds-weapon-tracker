from core.tracker import WeaponTracker
from ui.interface import TrackerUI
from utils.config_path import get_config_path

config_path = get_config_path()
tracker = WeaponTracker(config_path)
TrackerUI(tracker)
