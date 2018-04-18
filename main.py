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
        self.player = Player(self)
        self.all_sprites.add(self.player)

        for platform in PLATFORM_LIST:
            p = Platform(*platform)  # Take the list and explode it to list items
            self.all_sprites.add(p)
            self.platforms.add(p)

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

        # Check if player hits a platform WHILE falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        # If player reaches top part of the screen (1/4) scroll platforms down
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for platform in self.platforms:
                platform.rect.y += abs(self.player.vel.y)

                # Unload platforms that are not in game windows. (Window HEIGHT + 20%)
                if platform.rect.top >= (HEIGHT * 1.20):
                    platform.kill()

        # Spawn new platform to keep same avg of platforms
        while len(self.platforms) < 10:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),  # Generate X spawn cords.
                         random.randrange(-75, -30), # Generate Y spawn cords.
                         width, 20)  # Widtch of platform and HEIGHT of platform
            self.all_sprites.add(p)
            self.platforms.add(p)


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
