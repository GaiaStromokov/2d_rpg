from config.gen_import import *
from Enemy_class import Enemy


class Combat:
    def __init__(self, player, enemy):
        self.p = player
        self.e = Enemy(enemy,1)
        self.init_ui()
    def init_ui(self):
        with window(no_title_bar=True, pos=(20, 40), no_close=True, show=True,autosize=True,tag="CWin"):
            with group(horizontal=True):
                with child_window(border=True, auto_resize_y=True,auto_resize_x=True, tag="Pwin"):
                    add_button(label="Player", enabled=False)
                    with child_window(border=True, auto_resize_y=True,auto_resize_x=True, tag="Pchild"):
                        pass
                with child_window(border=True, auto_resize_y=True,auto_resize_x=True, tag="Ewin"):
                    add_button(label="Enemy", enabled=False)
                    with child_window(border=True, auto_resize_y=True,auto_resize_x=True, tag="Echild"):
                        pass
            with child_window(border=True, auto_resize_y=True,auto_resize_x=True, tag="Pact"):
                add_button(label="Player Actions", enabled=False)
        with window(no_title_bar=True, pos=(200, 40), no_close=True, show=True,tag="C_hist"):
            pass
