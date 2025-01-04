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






bg_dict = Box({
    "Prisoner": {
        "Pos": (7, 7),
        "Busy": False,
        "Level": 1,
        "Xp": 0,
        "Stats": {
            "Bod": 10,
            "Agi": 10,
            "Mnd": 10,
            "Vig": 10,
            "Str": 10,
            "Dex": 10,
            "Int": 10,
            "For": 10,
            "Poi": 10,
            "Dod": 10,
            "Wer": 10,
            "Gur": 10,
            "Wit": 10,
            "Cri": 10,
            "Ler": 10,
            "Luc": 0
        }
    }
})
stat_layout = [
    ["Bod", "Agi", "Mnd", "Vig"],
    ["Str", "Dex", "Int", "For"],
    ["Poi", "Dod", "Wer", "Gar"],
    ["Wit", "Cri", "Ler", "Luc"],  # None for unused slot
]



class Player:
    def __init__(self, bg):
        self.bg = bg
        self.pos = bg_dict[self.bg].Pos
        self.busy = bg_dict[self.bg].Busy
        self.tile = None
        self.L = bg_dict[self.bg].Level
        self.xp = bg_dict[self.bg].Xp
        
        
        
        self.vs = self.init_stats(bg_dict[self.bg].Stats, stat_layout)
        self.config_stats()
        self.ms = self.vs

        self.Inv=Inventory()
    
    def init_stats(self,stats, layout):
        matrix = np.zeros((4, 4), dtype=float)
        for i, row in enumerate(layout):
            for j, stat in enumerate(row):
                matrix[i, j] = stats.get(stat, 0)
        return matrix
    def config_stats(self):
        for i in range(3):
            for j in range(1, 3):
                self.vs[j, i] += self.c_stat(self.vs[j - 1, i])
            self.vs[3, i] = self.vs[:3, i].sum() * 0.33 
            self.vs[i, 3] = self.vs[i, :3].sum() * 0.33
        self.vs = self.vs.round(2)
    def c_stat(self,stat): return .011*(stat**2)
    def reset_stats(self): self.vs = self.ms
    def update_cs(self):
        stats = ["L", "xp", "Bod", "Agi", "Mnd", "Vig", "Str", "Dex", "Int", "For", "Poi", "Dod", "Wer", "Gur", "Wit", "Cri", "Ler", "Luc"]
        for stat in stats:
            configure_item(f"{stat}_cs", label=getattr(self, stat).V)




