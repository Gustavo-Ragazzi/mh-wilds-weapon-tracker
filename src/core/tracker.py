import json
from typing import Dict, Tuple
from dataclasses import dataclass

@dataclass
class Weapon:
  name: str
  primary: int = 0
  secondary: int = 0
  adjustment: int = 0

  def to_dict(self) -> dict:
    return { "primary": self.primary, "secondary": self.secondary, "adjustment": self.adjustment }


class WeaponTracker:
  def __init__(self, config_path: str):
    self.config_path = config_path
    self.weapons: Dict[str, Weapon] = self.load_weapons()

  def load_weapons(self) -> Dict[str, Weapon]:
    with open(self.config_path, "r") as f:
      data = json.load(f)
    return { name: Weapon(name, **usage) for name, usage in data.items() }

  def save_weapons(self) -> None:
    data = { name: weapon.to_dict() for name, weapon in self.weapons.items() }
    with open(self.config_path, "w") as f:
      json.dump(data, f, indent=2)

  def get_next_weapons(self) -> Tuple[Weapon, Weapon]:
    primary = next(w for w in self.weapons.values() if w.primary == self.get_min("primary"))
    secondary = next(w for w in self.weapons.values() if (w.secondary - w.adjustment) == self.get_min("secondary_with_adjustment"))
    return primary, secondary

  def advance(self) -> Tuple[str, str]:
    primary, secondary = self.get_next_weapons()
    primary.primary += 1
    secondary.secondary += 1
    self.save_weapons()
    return primary.name, secondary.name

  def get_max(self, field: str) -> int:
    return max(getattr(w, field) for w in self.weapons.values())

  def get_min(self, field: str) -> int:
    if field == "secondary_with_adjustment":
      return min(w.secondary - w.adjustment for w in self.weapons.values())
    return min(getattr(w, field) for w in self.weapons.values())
  
  def quests_remaining(self) -> Tuple[int, int]:
    max_primary = self.get_max("primary")
    primary_remain = sum(max_primary - w.primary for w in self.weapons.values())
    expected_secondary = {w.name: w.primary + w.adjustment for w in self.weapons.values()}
    max_secondary = max(expected_secondary.values())
    secondary_remain = sum(max_secondary - (w.secondary - w.adjustment) for w in self.weapons.values())
    return primary_remain, secondary_remain

