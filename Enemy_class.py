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
            "Stk": .75,
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
            "Stk": 1,
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
            "Stk": 1.25,
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
                "Stk": 10,
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
                "Stk": 10,
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

stat_layout = [
    ["Bod", "Agi", "Mnd", "Vig"],
    ["Str", "Dex", "Int", "For"],
    ["Poi", "Dod", "Wer", "Gar"],
    ["Wit", "Cri", "Ler", None],  # None for unused slot
]


class Enemy:
    def __init__(self, Name, cr):
        self.Name = Name
        self.Cr = cr
        self.Nature = list(n_dict.keys())[roll(len(n_dict)) - 1]
        self.vs = self.init_stats(m_dict[self.Name].Stats, stat_layout, self.Nature)
        self.config_stats()
        self.ms = self.vs

    def init_stats(self,stats, layout, nature):
        matrix = np.zeros((4, 4), dtype=float)
        for i, row in enumerate(layout):
            for j, stat in enumerate(row):
                if stat:
                    # Multiply the stat value by the corresponding nature's multiplier
                    matrix[i, j] = stats.get(stat, 0) * n_dict[nature].get(stat, 1)
        return matrix
    def config_stats(self):
        for i in range(3):
            for j in range(1, 3):
                self.vs[j, i] += self.c_stat(self.vs[j - 1, i])
            self.vs[3, i] = self.vs[:3, i].sum() * 0.33 
            self.vs[i, 3] = self.vs[i, :3].sum() * 0.33
        self.vs = self.vs.round(2)
    def reset_stats(self):
        self.vs = self.ms
    def c_stat(self,stat):
        return .011*(stat**2)
        
    


    def __str__(self):
        
        return (
            f"Mon Sheet: \n"
            f"Name: {self.Name}\n"
            f"CR: {self.Cr}\n"
            f"Nature: {self.Nature}\n"
            f"Stats:\n{self.ms}\n"
        )


# Test it
monster = Enemy("Goblin", 12)
print(monster)
