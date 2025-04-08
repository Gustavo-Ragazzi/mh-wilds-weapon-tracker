import os
from core.tracker import WeaponTracker
from ui.interface import TrackerUI

if __name__ == "__main__":
  config_path = os.path.join(os.path.dirname(__file__), "config", "weapons_config.json")
  tracker = WeaponTracker(config_path)
  TrackerUI(tracker)
