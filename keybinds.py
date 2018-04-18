# Holds common keybinds
import pygame as pg

pg.init()
keys = pg.key.get_pressed()

EXITGAME = keys[pg.K_LALT or pg.K_RALT]


JUMP_KEY = keys[pg.K_SPACE]