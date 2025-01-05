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



class Player:
    def __init__(self, bg):
        self.bg = bg
        self.pos = bg_dict[self.bg].Pos
        self.busy = bg_dict[self.bg].Busy
        self.tile = None
        self.L = bg_dict[self.bg].Level
        self.xp = bg_dict[self.bg].Xp
        self.stat = Box({
            "Bod": {'m': 0, 'v': 0},
            "Agi": {'m': 0, 'v': 0},
            "Mnd": {'m': 0, 'v': 0},
            "Vig": {'m': 0, 'v': 0},
            "Str": {'m': 0, 'v': 0},
            "Dex": {'m': 0, 'v': 0},
            "Int": {'m': 0, 'v': 0},
            "For": {'m': 0, 'v': 0},
            "Poi": {'m': 0, 'v': 0},
            "Dod": {'m': 0, 'v': 0},
            "Wer": {'m': 0, 'v': 0},
            "Gur": {'m': 0, 'v': 0},
            "Wit": {'m': 0, 'v': 0},
            "Cri": {'m': 0, 'v': 0},
            "Ler": {'m': 0, 'v': 0}
        })
        self.luc = 0
        self.init_stats()
        self.sm_calc()
        self.reset_stats()
        self.update_cs()
        self.Inv=Inventory()
    
    
    
    
    def init_stats(self):
        for stat in self.stat: self.stat[stat].m = m_dict[self.Name].Stats[stat] * n_dict[self.Nature][stat]
    def sm_calc(self):
        self.stat.Str.m = self.stat.Str.m + self.stat.Bod.m * .33
        self.stat.Dex.m = self.stat.Dex.m + self.stat.Agi.m * .33
        self.stat.Int.m = self.stat.Int.m + self.stat.Mnd.m * .33
        self.stat.Poi.m = self.stat.Poi.m + self.stat.Str.m * .33
        self.stat.Dod.m = self.stat.Dod.m + self.stat.Dex.m * .33
        self.stat.Wer.m = self.stat.Wer.m + self.stat.Int.m * .33
        self.stat.Vig.m = self.curve(self.stat.Bod.m) + self.curve(self.stat.Agi.m) + self.curve(self.stat.Mnd.m)
        self.stat.For.m = self.curve(self.stat.Str.m) + self.curve(self.stat.Dex.m) + self.curve(self.stat.Int.m)
        self.stat.Gur.m = self.curve(self.stat.Poi.m) + self.curve(self.stat.Dod.m) + self.curve(self.stat.Wer.m)
        self.stat.Wit.m = self.curve(self.stat.Bod.m) + self.curve(self.stat.Str.m) + self.curve(self.stat.Poi.m)
        self.stat.Cri.m = self.curve(self.stat.Agi.m) + self.curve(self.stat.Dex.m) + self.curve(self.stat.Dod.m)
        self.stat.Ler.m = self.curve(self.stat.Mnd.m) + self.curve(self.stat.Int.m) + self.curve(self.stat.Wer.m)
        for stat in self.stat: self.stat[stat].m = round(self.stat[stat].m)
    def sv_calc(self):
        self.stat.Str.v = self.stat.Bod.v * 0.33
        self.stat.Dex.v = self.stat.Agi.v * 0.33
        self.stat.Int.v = self.stat.Mnd.v * 0.33
        self.stat.Poi.v = self.stat.Str.v * 0.33
        self.stat.Dod.v = self.stat.Dex.v * 0.33
        self.stat.Wer.v = self.stat.Int.v * 0.33
        self.stat.Vig.v = self.curve(self.stat.Bod.v) + self.curve(self.stat.Agi.v) + self.curve(self.stat.Mnd.v)
        self.stat.For.v = self.curve(self.stat.Str.v) + self.curve(self.stat.Dex.v) + self.curve(self.stat.Int.v)
        self.stat.Gur.v = self.curve(self.stat.Poi.v) + self.curve(self.stat.Dod.v) + self.curve(self.stat.Wer.v)
        self.stat.Wit.v = self.curve(self.stat.Bod.v) + self.curve(self.stat.Str.v) + self.curve(self.stat.Poi.v)
        self.stat.Cri.v = self.curve(self.stat.Agi.v) + self.curve(self.stat.Dex.v) + self.curve(self.stat.Dod.v)
        self.stat.Ler.v = self.curve(self.stat.Mnd.v) + self.curve(self.stat.Int.v) + self.curve(self.stat.Wer.v)
        for stat in self.stat:
            self.stat[stat].v = round(self.stat[stat].m)
    def reset_stats(self):
        for stat in self.stat: self.stat[stat].v = self.stat[stat].m
    def curve(self,stat): return 0.011*(stat**2)
    def update_cs(self):
        configure_item(f"L_cs", label=self.L)
        configure_item(f"xp_cs", label=self.xp)
        configure_item(f"Luc_cs", label=self.luc)
        stats = ["Bod", "Agi", "Mnd", "Vig", "Str", "Dex", "Int", "For", "Poi", "Dod", "Wer"]
        for stat in stats: configure_item(f"{stat}_cs", label=self.stat[stat].v)




