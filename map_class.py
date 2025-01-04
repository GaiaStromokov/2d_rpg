from config.gen_import import *
from Encounters import *
os.system('cls' if os.name == 'nt' else 'clear')
base_map = pd.read_csv("config/mapfile/base_map.csv", header=None)


td=Box({
    "p": {'Color':cm.player},
    '' : {'Walk': True, 'Color': cm.tp},
    'Path': {'Walk': True, 'Color': cm.Path},
    'Forest': {'Walk': True, 'Color': cm.Forest},
    'Sand': {'Walk': True, 'Color': cm.Sand},
    'Water': {'Walk': False, 'Color': cm.Water},
    'Wall': {'Walk': False, 'Color': cm.Wall}
})


map_csv_d = {
    9: 'Path',
    25: 'Forest',
    17: 'Sand',
    33: 'Water',
    65: 'Wall',
    
}

class Map:
    def __init__(self, player):
        self.player = player
        self.gmap_w = 50
        self.gmap_h = 50
        self.gmap = np.full((self.gmap_w, self.gmap_h, 2), '', dtype=object)
        self.ts = 20
        self.vr = 7
        self.init_map()
        self.draw_map()
    def init_map(self):
        self.gmap[:, :, 0] = base_map.replace(map_csv_d).to_numpy()
        self.gmap[:, :, 1] = ''
        set_value("Pos_bug", f"{self.player.pos[1]}, {self.player.pos[0]}")
        set_value("Loc_bug", f"{self.gmap[self.player.pos[0], self.player.pos[1], 0]}, {self.gmap[self.player.pos[0], self.player.pos[1], 1]}")
        set_value("Tile_bug", f"{self.player.tile}")
        

    def draw_map(self):
        delete_item("map_dl", children_only=True)
        
        cr, cc = self.player.pos  
        g_start= [max(cr - self.vr, 0),max(cc - self.vr, 0)]
        g_end= [min(cr + self.vr + 1, self.gmap_h),min(cc + self.vr + 1, self.gmap_w)]
        g_offset = [max(self.vr - cr, 0),max(self.vr - cc, 0)]

        for r in range(g_start[0], g_end[0]):
            for c in range(g_start[1], g_end[1]):
                rmin = ((c - g_start[1] + g_offset[1])*self.ts,(r - g_start[0] + g_offset[0])*self.ts)
                rmax = ((c - g_start[1] + g_offset[1] + 1)*self.ts,(r - g_start[0] + g_offset[0] + 1)*self.ts)
                for l in range(2):
                    color=td[self.gmap[r, c, l]].Color
                    draw_rectangle(pmin=rmin,pmax=rmax,color=color, fill=color, parent="map_dl")
        draw_rectangle(pmin=(7*self.ts,7*self.ts),pmax=(8*self.ts,8*self.ts),color=td.p.Color,fill=td.p.Color,parent="map_dl",thickness=1)



kp_d = {
    513: "la",
    514: "ra",
    515: "ua",
    516: "da",
}


class KeyPress:
    def __init__(self, movement):
        self.kd = kp_d
        self.movement = movement

    def kp(self, sender, key):
        if key in self.kd and key in [513, 514, 515, 516]:
            self.movement.move_input(sender, key)


class Movement:
    def __init__(self, player, map_class, encounter_class):
        self.player = player
        self.m = map_class
        self.e = encounter_class
        self.deltas = {513: (0, -1), 514: (0, 1), 515: (-1, 0), 516: (1, 0)}


    def move_input(self, s, k):
        if self.player.busy:
            return
        dr, dc = self.deltas[k]
        nr, nc = self.player.pos[0] + dr, self.player.pos[1] + dc
        if self.is_walkable(nr, nc):
            self.player.pos = (nr, nc)
            self.m.draw_map()
            self.update_tile()
            self.update_ui()
            self.e.check_encounter()
    def is_walkable(self, r, c):
        return 0 <= r < self.m.gmap_h and 0 <= c < self.m.gmap_w and td[self.m.gmap[r, c, 0]].Walk and td[self.m.gmap[r, c, 1]].Walk
    def update_tile(self):
        if  self.m.gmap[self.player.pos[0], self.player.pos[1], 1] == '':
            self.player.tile = self.m.gmap[self.player.pos[0], self.player.pos[1], 0]
        else:
            self.player.tile = self.m.gmap[self.player.pos[0], self.player.pos[1], 1]
    def update_ui(self):
        set_value("Pos_bug", f"{self.player.pos[1]}, {self.player.pos[0]}")
        set_value("Loc_bug", f"{self.m.gmap[self.player.pos[0], self.player.pos[1], 0]}, {self.m.gmap[self.player.pos[0], self.player.pos[1], 1]}")
        set_value("Tile_bug", f"{self.player.tile}")
