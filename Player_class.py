from config.gen_import import *


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
        self.Weight = None
        self.Hands = None
        self.Type = None
        self.Length = None
        self.die = None
        self.scale = None

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
        self.init_ui()
    def init_ui(self):
        delete_item("Inventory", children_only=True)
        with group(parent="Inventory"):
            for key in self.Bag.d.keys():
                with tree_node(label=key):
                    pass
            
#------------------------------------------------------------------
class Stat:
    def __init__(self, value: float = 0.0):
        self.M = value  # Max value
        self.V = value  # Current value

class Player:
    def __init__(self, pos, busy, level, exp, Bod, Mnd, Luc, Hrt, Agi, Spc, Str, Dex, Int, Poi, Dod, Wer, Mom):
        self.pos = pos
        self.tile = None
        self.busy = busy
        self.L = Stat(level)
        self.xp = Stat(exp)
        self.csview = False
        self.Bod = Stat(Bod)
        self.Mnd = Stat(Mnd)
        self.Luc = Stat(Luc)
        self.Hrt = Stat(Hrt)
        self.Agi = Stat(Agi)
        self.Spc = Stat(Spc)
        self.Str = Stat(Str)
        self.Dex = Stat(Dex)
        self.Int = Stat(Int)
        self.Poi = Stat(Poi)
        self.Dod = Stat(Dod)
        self.Wer = Stat(Wer)
        self.Mom = Mom
        self.Inv=Inventory()
    
    def update_cs(self):
        stats = ["L", "xp", "Bod", "Mnd", "Luc", "Hrt", "Agi", "Spc", "Str", "Dex", "Int", "Poi", "Dod", "Wer"]
        for stat in stats:
            configure_item(f"{stat}_cs", label=getattr(self, stat).V)
            






