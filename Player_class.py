from config.gen_import import *
from Inventory_class import Inventory
stl = ["Bod","Agi","Mnd","Vig","Str","Dex","Int","For","Poi","Dod","Wer","Gur","Wit","Cri", "Ler"]


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
        },
        "Luc": 0,
        "Items": {
            "Weapons": ["Shiv"]
        }
    }
})

class Stat():
    def __init__(self, m, v):
        self.m = m
        self.v = v

class Player:
    def __init__(self, bg):
        self.bg = bg
        self.pos = bg_dict[self.bg].Pos
        self.busy = bg_dict[self.bg].Busy
        self.tile = None
        self.L = bg_dict[self.bg].Level
        self.xp = bg_dict[self.bg].Xp
        self.hp=Stat(0,0)
        self.Bod = Stat(bg_dict[self.bg].Stats.Bod, bg_dict[self.bg].Stats.Bod)
        self.Agi = Stat(bg_dict[self.bg].Stats.Agi, bg_dict[self.bg].Stats.Agi)
        self.Mnd = Stat(bg_dict[self.bg].Stats.Mnd, bg_dict[self.bg].Stats.Mnd)
        self.Vig = Stat(0,0)
        self.Str = Stat(bg_dict[self.bg].Stats.Str, bg_dict[self.bg].Stats.Str)
        self.Dex = Stat(bg_dict[self.bg].Stats.Dex, bg_dict[self.bg].Stats.Dex)
        self.Int = Stat(bg_dict[self.bg].Stats.Int, bg_dict[self.bg].Stats.Int)
        self.For = Stat(0,0)
        self.Poi = Stat(bg_dict[self.bg].Stats.Poi, bg_dict[self.bg].Stats.Poi)
        self.Dod = Stat(bg_dict[self.bg].Stats.Dod, bg_dict[self.bg].Stats.Dod)
        self.Wer = Stat(bg_dict[self.bg].Stats.Wer, bg_dict[self.bg].Stats.Wer)
        self.Gur = Stat(0,0)
        self.Wit = Stat(0,0)
        self.Cri = Stat(0,0)
        self.Ler = Stat(0,0)
        self.luc = bg_dict[self.bg].Luc
        self.sm_calc()
        self.reset_stats()
        self.update_cs()
        self.Inv=Inventory()
        for item in bg_dict[self.bg].Items.Weapons: self.Inv.Bag.d.Weapons[item] = Box({"Name": item, "Quality": 10})
        self.Inv.update_ui()

    def sm_calc(self):
        self.Str.m = self.Str.m + self.Bod.m * .33
        self.Dex.m = self.Dex.m + self.Agi.m * .33
        self.Int.m = self.Int.m + self.Mnd.m * .33
        self.Poi.m = self.Poi.m + self.Str.m * .33
        self.Dod.m = self.Dod.m + self.Dex.m * .33
        self.Wer.m = self.Wer.m + self.Int.m * .33
        self.Vig.m = self.curve(self.Bod.m) + self.curve(self.Agi.m) + self.curve(self.Mnd.m)
        self.For.m = self.curve(self.Str.m) + self.curve(self.Dex.m) + self.curve(self.Int.m)
        self.Gur.m = self.curve(self.Poi.m) + self.curve(self.Dod.m) + self.curve(self.Wer.m)
        self.Wit.m = self.curve(self.Bod.m) + self.curve(self.Str.m) + self.curve(self.Poi.m)
        self.Cri.m = self.curve(self.Agi.m) + self.curve(self.Dex.m) + self.curve(self.Dod.m)
        self.Ler.m = self.curve(self.Mnd.m) + self.curve(self.Int.m) + self.curve(self.Wer.m)
        for stat in stl: getattr(self, stat).m = round(getattr(self, stat).m,2)
        self.hp.m = round(self.Vig.m*2.1,2)
    def sv_calc(self):
        self.Str.v = self.Bod.v * 0.33
        self.Dex.v = self.Agi.v * 0.33
        self.Int.v = self.Mnd.v * 0.33
        self.Poi.v = self.Str.v * 0.33
        self.Dod.v = self.Dex.v * 0.33
        self.Wer.v = self.Int.v * 0.33
        self.Vig.v = self.curve(self.Bod.v + self.Agi.v + self.Mnd.v)
        self.For.v = self.curve(self.Str.v + self.Dex.v + self.Int.v)
        self.Gur.v = self.curve(self.Poi.v + self.Dod.v + self.Wer.v)
        self.Wit.v = self.curve(self.Bod.v + self.Str.v + self.Poi.v)
        self.Cri.v = self.curve(self.Agi.v + self.Dex.v + self.Dod.v)
        self.Ler.v = self.curve(self.Mnd.v + self.Int.v + self.Wer.v)
        for stat in stl: getattr(self, stat).v = round(getattr(self, stat).v,2)
        self.hp.v = round(self.hp.v-((self.Vig.m-self.Vig.v)*2.1),2)
    def reset_stats(self):
        for stat in stl: getattr(self, stat).v = getattr(self, stat).m
        self.hp.v = self.hp.m
    def curve(self,stat): return 0.011*(stat**2)
    def update_cs(self):
        configure_item(f"L_cs", label=self.L)
        configure_item(f"xp_cs", label=self.xp)
        configure_item(f"Luc_cs", label=self.luc)
        configure_item(f"hp_cs", label=f'{round(self.hp.v,1)}/{round(self.hp.m,1)}')
        for stat in ["Bod", "Agi", "Mnd", "Str", "Dex", "Int", "Poi", "Dod", "Wer"]: 
            configure_item(f"{stat}_cs", label=getattr(self, stat).v)
            




