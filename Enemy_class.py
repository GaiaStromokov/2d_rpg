from config.gen_import import *
os.system('cls' if os.name == 'nt' else 'clear')
def roll(sides): return random.randint(1, sides)


n_dict = Box({
    "Weak": {
        "Bod": .75,
        "Mnd": .75,
        "Hrt": .75,
        "Agi": .75,
        "Str": .75,
        "Dex": .75,
        "Int": .75,
        "Poi": .75,
        "Dod": .75,
        "Wer": .75
    },
    "Normal": {
        "Bod": 1,
        "Mnd": 1,
        "Hrt": 1,
        "Agi": 1,
        "Str": 1,
        "Dex": 1,
        "Int": 1,
        "Poi": 1,
        "Dod": 1,
        "Wer": 1
    },
    "Strong": {
        "Bod": 1.25,
        "Mnd": 1.25,
        "Hrt": 1.25,
        "Agi": 1.25,
        "Str": 1.25,
        "Dex": 1.25,
        "Int": 1.25,
        "Poi": 1.25,
        "Dod": 1.25,
        "Wer": 1.25
    },
})
m_dict = Box({
    "Bandit": {
        "Stats": {
            "Bod": 10,
            "Mnd": 10,
            "Hrt": 10,
            "Agi": 10,
            "Str": 10,
            "Dex": 10,
            "Int": 10,
            "Poi": 10,
            "Dod": 10,
            "Wer": 10
        },
        "Actions": {
            "Attacks": ["Slash", "Super"]
        }
    },
    "Goblin": {
        "Stats": {
            "Bod": 10,
            "Mnd": 10,
            "Hrt": 10,
            "Agi": 10,
            "Str": 10,
            "Dex": 10,
            "Int": 10,
            "Poi": 10,
            "Dod": 10,
            "Wer": 10
        },
        "Actions": {
            "Attacks": ["Slash", "Super"]
        }
    }
})






class Enemy:
    def __init__(self, Name, cr):
        self.Name = Name
        self.Cr = cr
        self.Nature = list(n_dict.keys())[roll(len(n_dict)) - 1]
        self.Stats = Box({stat: {"B": (base := m_dict[Name].Stats[stat] * n_dict[self.Nature][stat]), "V": base} for stat in m_dict[Name].Stats})
        self.Stats.Hrt.B = round(self.Stats.Hrt.B + self.c_stat(self.Stats.Bod.B) + self.c_stat(self.Stats.Mnd.B), 2)
        self.Stats.Agi.B = round(self.Stats.Agi.B + self.c_stat(self.Stats.Bod.B) + self.c_stat(self.Stats.Mnd.B), 2)
        self.Stats.Str.B = round(self.Stats.Str.B + self.c_stat(self.Stats.Bod.B) + self.c_stat(self.Stats.Mnd.B), 2)
        self.Stats.Dex.B = round(self.Stats.Dex.B + self.c_stat(self.Stats.Agi.B), 2)
        self.Stats.Int.B = round(self.Stats.Int.B + self.c_stat(self.Stats.Mnd.B), 2)
        self.Stats.Poi.B = round(self.Stats.Poi.B + self.c_stat(self.Stats.Hrt.B) + self.c_stat(self.Stats.Mnd.B) + self.c_stat(self.Stats.Bod.B), 2)
        self.Stats.Dod.B = round(self.Stats.Dod.B + self.c_stat(self.Stats.Agi.B) + self.c_stat(self.Stats.Dex.B), 2)
        self.Stats.Wer.B = round(self.Stats.Wer.B + self.c_stat(self.Stats.Int.B)+ self.c_stat(self.Stats.Mnd.B), 2)
        self.reset_stats()
    
    def config_stats(self):
        self.Stats.Hrt.V = round(self.Stats.Hrt.V + self.c_stat(self.Stats.Bod.V) + self.c_stat(self.Stats.Mnd.V), 2)
        self.Stats.Agi.V = round(self.Stats.Agi.V + self.c_stat(self.Stats.Bod.V) + self.c_stat(self.Stats.Mnd.V), 2)
        self.Stats.Str.V = round(self.Stats.Str.V + self.c_stat(self.Stats.Bod.V) + self.c_stat(self.Stats.Mnd.V), 2)
        self.Stats.Dex.V = round(self.Stats.Dex.V + self.c_stat(self.Stats.Agi.V), 2)
        self.Stats.Int.V = round(self.Stats.Int.V + self.c_stat(self.Stats.Mnd.V), 2)
        self.Stats.Poi.V = round(self.Stats.Poi.V + self.c_stat(self.Stats.Hrt.V) + self.c_stat(self.Stats.Mnd.V) + self.c_stat(self.Stats.Bod.V), 2)
        self.Stats.Dod.V = round(self.Stats.Dod.V + self.c_stat(self.Stats.Agi.V) + self.c_stat(self.Stats.Dex.V), 2)
        self.Stats.Wer.V = round(self.Stats.Wer.V + self.c_stat(self.Stats.Int.V)+ self.c_stat(self.Stats.Mnd.V), 2)
    def c_stat(self, stat):
        return 0.011*(stat**2)
    def reset_stats(self):
        for stat in self.Stats:
            self.Stats[stat].V = self.Stats[stat].B
        
    def __str__(self):
        stats_str = "\n".join(f"  {stat}: B = {self.Stats[stat]['B']}, V = {self.Stats[stat]['V']}"for stat in self.Stats)
        return (
            f"Mon Sheet: \n"
            f"Name: {self.Name}\n"
            f"CR: {self.Cr}\n"
            f"Nature: {self.Nature}\n"
            f"Stats:\n{stats_str}\n"
        )
        
    

# Test it
monster = Enemy('Goblin', 12)
print(monster)
