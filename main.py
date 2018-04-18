# RPG Main Executable

import pygame as pg
import random

from settings import *
from sprites import *
from keybinds import *

class Game:
    def __init__(self):
        # initialize game window, etc

        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE + " | FPS: " + str(int(self.clock.get_fps())))
        self.running = True

    def new(self):
        # Restarts game / Start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform(WIDTH / 2 -50, HEIGHT * 3 /4, 100, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)




    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()
        print(str(int(self.clock.get_fps())))

        # Colision check
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top + 1
            self.player.vel.y = 0

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            # Jumping
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def show_start_screen(self):
        # Game splash screen
        pass

    def show_gameover_screen(self):
        # Game over screen
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_gameover_screen()

pg.quit()
