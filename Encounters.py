from config.gen_import import *
from Combat import Combat
def rh(): return random.randint(1, 100)

re_dl=["Path","Forest","Sand"]
re_d = Box({
    "Path": {
        "pc": 0,
        "enc": {}
    },
    "Forest": {
        "pc": 25,
        "enc": {
            "Goblin": 75,
            "Bandit": 25
        }
    },
    "Sand": {
        "pc": 25,
        "enc": {
            "Worm": 75,
            "Lizard": 25
        }
    }
})


class EncounterManager:
    def __init__(self, player):
        self.p = player

    def check_encounter(self):
        self.tile = self.p.tile
        if self.tile in re_dl:
            if rh() <= re_d[self.tile].pc:
                self.p.busy = True
                self.rand_enc_staging(random.choices(list(re_d[self.tile].enc.keys()), weights=list(re_d[self.tile].enc.values()), k=1)[0])
            else:
                pass
        else:
            pass
            

    def rand_enc_staging(self, enemy):
        combat = Combat(self.p,enemy)





