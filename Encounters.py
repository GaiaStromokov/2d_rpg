from config.gen_import import *

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




class Rand_Encounter:
    def __init__(self, tile):
        self.tile = tile
        self.pc = re_d[tile].pc
        self.list = re_d[tile].enc

class EncounterManager:
    def __init__(self, player):
        self.p = player

    def check_encounter(self):
        self.tile = self.p.tile
        if self.tile in re_dl:
            enc = Rand_Encounter(self.tile)
            if rh() <= enc.pc:
                self.rand_enc_staging(random.choices(list(enc.list.keys()), weights=list(enc.list.values()), k=1)[0])
            else:
                print("No random encounter occurred.")
        else:
            print("other encounters too come")
            

    def rand_enc_staging(self, encounter):
        pass


