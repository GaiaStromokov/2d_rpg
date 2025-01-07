from config.gen_import import *
from Weapon_class import *
class Bag:
    def __init__(self):
        self.d = Box({
            "Weapons": {
                
            },
            "Armor": {
                
            },
        })
class WSL:
    def __init__(self):
        self.Name = None
        self.Quality  = None
        self.Type = None
        self.Speed = None
        self.Weight = None
        self.Crit = None
        self.Scaling = None
        self.Actions = None

class ASL:
    def __init__(self):
        self.Name = None
        self.Weight = None
        self.Type = None

class Inventory:
    def __init__(self):
        self.Hand1 = WSL()
        self.Hand2 = WSL()
        self.Helm = ASL()
        self.Chest = ASL()
        self.Legs = ASL()
        self.Boots = ASL()
        self.Gloves = ASL()
        self.Bag = Bag()
        self.update_ui()
    def update_ui(self):
        delete_item("Inventory", children_only=True)
        with group(parent="Inventory"):
            for key in self.Bag.d.keys():
                with tree_node(label=key):
                    for item_name in self.Bag.d[key].keys():
                        add_text
    def update_ui(self):
        delete_item("Inventory", children_only=True)
        with group(parent="Inventory"):
            for category in self.Bag.d.keys():
                with tree_node(label=category):
                    for idx, (item_name, item_data) in enumerate(self.Bag.d[category].items(), start=1):
                        tag = f"{category.lower()}_{idx}"  # e.g., "weapon_1", "armor_2"
                        add_selectable(label=item_name, tag=tag)
                        with tooltip(tag):
                            add_text(f"Name: {item_data['Name']}")
                            add_text(f"Type: {item_data['Type']}")
                            add_text(f"Speed: {item_data['Speed']}")
                            add_text(f"Weight: {item_data['Weight']}")
                            add_text(f"Crit: {item_data['Crit']}")
                            add_text(f"Scaling: {item_data['Scaling']}")
                            add_text(f"Actions: {item_data['Actions']}")
                            add_text(f"Quality: {item_data['Quality']}")



