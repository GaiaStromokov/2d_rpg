from config.gen_import import *
os.system('cls' if os.name == 'nt' else 'clear')
def roll(sides): return random.randint(1, sides)


nature_dict = Box({
    "Weak": {
        "Bod": "E",
        "Mnd": "E",
        "Hrt": "E",
        "Agi": "E",
        "Str": "E",
        "Dex": "E",
        "Int": "E",
        "Poi": "E",
        "Dod": "E",
        "Wer": "E"
    },
    "Normal": {
        "Bod": "C",
        "Mnd": "C",
        "Hrt": "C",
        "Agi": "C",
        "Str": "C",
        "Dex": "C",
        "Int": "C",
        "Poi": "C",
        "Dod": "C",
        "Wer": "C"
    },
    "Strong": {
        "Bod": "A",
        "Mnd": "A",
        "Hrt": "A",
        "Agi": "A",
        "Str": "A",
        "Dex": "A",
        "Int": "A",
        "Poi": "A",
        "Dod": "A",
        "Wer": "A"
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
        self.Nature = list(nature_dict.keys())[roll(len(nature_dict)) - 1]
        self.Stats = Box({stat: {"B": (base := m_dict[Name].Stats[stat] + nature_dict[self.Nature][stat]), "V": base} for stat in m_dict[Name].Stats})

    def config_stats(self):
        self.Stats.Hrt.B = self.Stats.Hrt.B + self.Stats.Bod.B 
        self.Stats.Agi.B = self.Stats.Agi.B      
        self.Stats.Str.B = self.Stats.Str.B      
        self.Stats.Dex.B = self.Stats.Dex.B      
        self.Stats.Int.B = self.Stats.Int.B      
        self.Stats.Pos.B = self.Stats.Pos.B      
        self.Stats.Dod.B = self.Stats.Dod.B      
        self.Stats.Wer.B = self.Stats.Wer.B      
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
