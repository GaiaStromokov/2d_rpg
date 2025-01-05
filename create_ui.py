from config.gen_import import *

def create_map():
    with window(no_title_bar=True, pos=(500,200), no_close=True, tag="map_window"):
        with child_window(border=True,auto_resize_x=True, auto_resize_y=True, tag="map_child"):
            add_drawlist(width=300, height=300, tag="map_dl")

def create_debug_menu():
    with window(label='Debug_menu', pos=(500,350), no_close=True,width=320, height=200, tag="debug_window"):
        with child_window(border=True, auto_resize_x=True, auto_resize_y=True, tag="debug_child"):
            with group(horizontal=True):
                add_button(label='POS', enabled=False)
                add_text("", tag='Pos_bug')
            with group(horizontal=True):
                add_button(label='Loc', enabled=False)
                add_text("", tag='Loc_bug')
            with group(horizontal=True):
                add_button(label='Tile', enabled=False)
                add_text("", tag='Tile_bug')


# "L", "xp", "Bod", "Agi", "Mnd", "Vig", "Str", "Dex", "Int", "For", "Poi", "Dod", "Wer", "Gur", "Wit", "Cri", "Ler", "Luc"]
def create_chs():
    with window(no_title_bar=True, pos=(0, 0), no_close=True, show=True,tag="CS_window"):
        with group (horizontal=True):
            with child_window(border=True, auto_resize_y=True,auto_resize_x=True, tag="stats"):
                with group (horizontal=True):
                    with child_window(height=58, width=55, border=True):
                        add_button(label='LvL', enabled=False,width=40)
                        add_button(label='', enabled=False,width=40, tag="L_cs")
                    with child_window(height=58, width=55, border=True):
                        add_button(label='EXP', enabled=False,width=40)
                        add_button(label='', enabled=False,width=40,tag="xp_cs")
                with group (horizontal=True):
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Bod', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Bod_cs")
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Str', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Str_cs")
                with group (horizontal=True):
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Agi', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Agi_cs")
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Dex', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Dex_cs")
                with group (horizontal=True):
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Mnd', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Mnd_cs")
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Int', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Int_cs")
                with group (horizontal=True):
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Poi', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Poi_cs")
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Dod', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Dod_cs")
                with group (horizontal=True):
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Wer', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Wer_cs")
                    with child_window(height=58, width=55, border=True):
                        add_button(label='Luc', enabled=False, width=40)
                        add_button(label="", enabled=False, width=40, tag="Luc_cs")
            with child_window(border=True, auto_resize_x=True, auto_resize_y=True, tag="Equipment"):
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True, tag="E_inv"):
                    with group(horizontal=True):
                        add_button(label="Hand 1", enabled=False,width=50)
                        add_button(label="", enabled=False, tag="H1_inv")
                    with group(horizontal=True):
                        add_button(label="Hand 2", enabled=False,width=50)
                        add_button(label="", enabled=False, tag="H2_inv")
                    with group(horizontal=True):
                        add_button(label="Helm", enabled=False,width=50)
                        add_button(label="", enabled=False, tag="Helm_inv")
                    with group(horizontal=True):
                        add_button(label="Chest", enabled=False,width=50)
                        add_button(label="", enabled=False, tag="Chest_inv")
                    with group(horizontal=True):
                        add_button(label="Legs", enabled=False,width=50)
                        add_button(label="", enabled=False, tag="Legs_inv")
                    with group(horizontal=True):
                        add_button(label="Boots", enabled=False,width=50)
                        add_button(label="", enabled=False, tag="Boots_inv")
                    with group(horizontal=True):
                        add_button(label="Gloves", enabled=False, width=50)
                        add_button(label="", enabled=False, tag="Gloves_inv")
            with child_window(border=True,auto_resize_y=True, tag="Inventory"):
                    pass