from config.gen_import import *
from config.sub_import import *

os.system('cls' if os.name == 'nt' else 'clear')
def roll(sides): return random.randint(1, sides)


class Game:
    def __init__(self):
        self.init_ui()
        self.init_player()
        self.init_map()
        self.init_keys()
    def init_player(self):
        self.p=Player("Prisoner")
        self.p.update_cs()
    def init_ui(self):
        create_map()
        create_debug_menu()
        create_chs()
    def init_map(self):
        self.m = Map(self.p)
        self.m.init_map()
    def init_keys(self):
        self.e = EncounterManager(self.p)
        self.move=Movement(self.p, self.m, self.e)
        self.key_M = KeyPress(self.move)
        with handler_registry(): add_key_press_handler(callback=self.key_M.kp)
        




create_context()
with font_registry(): font_choice = add_font("config/Helvetica.ttf", 13)
configure_app(init_file="config/config_save.ini", docking=True, docking_space=True)
create_viewport(title="rpg", width=1400, height=800)
bind_font(font_choice)
setup_dearpygui()
g=Game()


show_viewport()
start_dearpygui()
destroy_context()
save_init_file("config/config_save.ini")
