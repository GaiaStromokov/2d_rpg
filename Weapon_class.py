from config.gen_import import *


weapon_list = ["Shiv", "Stiletto", "Broadsword", "Rapier", "Battle Axe", "Hand Axe", "Warhammer", "Mace"]
Arm_dict = Box({
    "Dagger": {
        "Shiv": {
            "Type": "Piercing",
            "Speed": 5,
            "Weight": 2,
            "Crit": 0.10,
            "Scaling": {"Str": "D+", "Dex": "B", "Int": "E+"},
            "Actions": ["Dirty Strike", "Quick Thrust", "Gut", "Makeshift Poison"]
        },
        "Stiletto": {
            "Type": "Piercing",
            "Speed": 5,
            "Weight": 1,
            "Crit": 0.30,
            "Scaling": {"Str": "C+", "Dex": "B+", "Int": "D++"},
            "Actions": ["Armor Pierce", "Quick Thrust", "Gut", "Kidney Shot"]
        }
    },
    "Straight Sword": {
        "Broadsword": {
            "Type": "Slashing",
            "Speed": 3,
            "Weight": 4,
            "Crit": 0.01,
            "Scaling": {"Str": "B++", "Dex": "C+", "Int": "E++"},
            "Actions": ["Wide Arc", "Slash", "Maim", "Shield Break"]
        },
        "Rapier": {
            "Type": "Piercing",
            "Speed": 4,
            "Weight": 3,
            "Crit": 0.10,
            "Scaling": {"Str": "D", "Dex": "B+", "Int": "D+"},
            "Actions": ["Lunge", "Slash", "Gut", "Riposte"]
        }
    },
    "Axe": {
        "Battle Axe": {
            "Type": "Slashing",
            "Speed": 3,
            "Weight": 6,
            "Crit": 0.01,
            "Scaling": {"Str": "B+", "Dex": "D+", "Int": "E++"},
            "Actions": ["Brutal Chop", "Cleave", "Maim", "Execution"]
        },
        "Hand Axe": {
            "Type": "Slashing",
            "Speed": 4,
            "Weight": 4,
            "Crit": 0.01,
            "Scaling": {"Str": "C++", "Dex": "C+", "Int": "E+"},
            "Actions": ["Swift Strike", "Cleave", "Maim", "Throw Axe"]
        }
    },
    "Hammer": {
        "Warhammer": {
            "Type": "Blunt",
            "Speed": 2,
            "Weight": 8,
            "Crit": 0.01,
            "Scaling": {"Str": "B+", "Dex": "E+", "Int": "E+"},
            "Actions": ["Overhead Smash", "Pound", "Crush", "Skull Crusher"]
        },
        "Mace": {
            "Type": "Blunt",
            "Speed": 2,
            "Weight": 5,
            "Crit": 0.01,
            "Scaling": {"Str": "B+", "Dex": "D++", "Int": "E++"},
            "Actions": ["Side Swing", "Pound", "Crush", "Concussion"]
        }
    }
})


sval = {
    "E": 0.01, "E+": 0.11, "E++": 0.21,
    "D": 0.32, "D+": 0.42, "D++": 0.52,
    "C": 0.62, "C+": 0.73, "C++": 0.83,
    "B": 0.93, "B+": 1.03, "B++": 1.14,
    "A": 1.24, "A+": 1.34, "A++": 1.44,
    "S": 1.55, "S+": 1.65, "S++": 1.75
}


class Weapon:
    def __init__(self, Name, Quality):
        self.Name = Name
        self.Quality = Quality
        
        # Locate weapon data
        wdata = next(weapon for category in Arm_dict.values() for weapon_name, weapon in category.items() if weapon_name == Name)
        
        self.Type = wdata.Type
        self.Speed = wdata.Speed
        self.Weight = wdata.Weight
        self.Crit = wdata.Crit
        
        # Calculate scaling based on quality
        self.Scaling = {
            stat: round(min(max(sval[grade] + (qmod := (Quality - 10) * 0.05), 0.01), 1.75 + max(0, qmod / 2)), 2)
            for stat, grade in wdata.Scaling.items()
        }
        
        self.Actions = wdata.Actions