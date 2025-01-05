from config.gen_import import *

os.system("cls" if os.name == "nt" else "clear")


def roll(sides):
    return random.randint(1, sides)


n_dict = Box(
    {
        "Weak": {
            "Bod": .75,
            "Agi": .75,
            "Mnd": .75,
            "Vig": .75,
            "Str": .75,
            "Dex": .75,
            "Int": .75,
            "For": .75,
            "Poi": .75,
            "Dod": .75,
            "Wer": .75,
            "Gur": .75,
            "Wit": .75,
            "Cri": .75,
            "Ler": .75,
        },
        "Normal": {
            "Bod": 1,
            "Agi": 1,
            "Mnd": 1,
            "Vig": 1,
            "Str": 1,
            "Dex": 1,
            "Int": 1,
            "For": 1,
            "Poi": 1,
            "Dod": 1,
            "Wer": 1,
            "Gur": 1,
            "Wit": 1,
            "Cri": 1,
            "Ler": 1,
        },
        "Strong": {
            "Bod": 1.25,
            "Agi": 1.25,
            "Mnd": 1.25,
            "Vig": 1.25,
            "Str": 1.25,
            "Dex": 1.25,
            "Int": 1.25,
            "For": 1.25,
            "Poi": 1.25,
            "Dod": 1.25,
            "Wer": 1.25,
            "Gur": 1.25,
            "Wit": 1.25,
            "Cri": 1.25,
            "Ler": 1.25,
        },
    }
)
m_dict = Box(
    {
        "Bandit": {
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
            "Actions": {"Attacks": ["Slash", "Super"]},
        },
        "Goblin": {
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
            "Actions": {"Attacks": ["Slash", "Super"]},
        },
    }
)




class Enemy:
    def __init__(self, Name, cr):
        self.Name = Name
        self.Cr = cr
        self.Nature = list(n_dict.keys())[roll(len(n_dict)) - 1]
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
        self.init_stats()
        self.sm_calc()
        self.reset_stats()

    
    def init_stats(self):
        for stat in self.stat:
            self.stat[stat].m = m_dict[self.Name].Stats[stat] * n_dict[self.Nature][stat]
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
        for stat in self.stat:
            self.stat[stat].m = round(self.stat[stat].m)
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
        for stat in self.stat:
            self.stat[stat].v = self.stat[stat].m
    def curve(self,stat):
        return 0.011*(stat**2)
    def __str__(self):
        stats_str = "\n".join([f"{key}: m:{self.stat[key].m}, v:{self.stat[key].v}" for key in self.stat])
        return (
            f"Mon Sheet:\n"
            f"Name: {self.Name}\n"
            f"CR: {self.Cr}\n"
            f"Nature: {self.Nature}\n"
            f"Stats:\n{stats_str}\n"
        )


# Test it
monster = Enemy("Goblin", 12)
print(monster)
