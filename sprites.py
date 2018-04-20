import pygame as pg
from tilemap import collide_hit_rect
from settings import *

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(x=0, y=0)
        self.pos = vec(x=x, y=y) * TILESIZE
        self.rotation = 0

    def get_keys(self):
        self.rotation_speed = 0
        self.vel = vec(x=0, y=0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rotation_speed = PLAYER_ROTATION_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rotation_speed = -PLAYER_ROTATION_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(x=PLAYER_SPEED, y=0).rotate(-self.rotation)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(x=-PLAYER_SPEED / 2, y=0).rotate(self.rotation)
        if keys[pg.K_q]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_e]:
            self.vel.x = PLAYER_SPEED

        # Detect diagonal movement and apply pythagoras theorem
        # This will keep the speed of diagonal movements the same
        # with horizontal / vertical movement
        # if (self.vel.x != 0) and (self.vel.y != 0):
        #     self.vel *= 0.7071
        # DON'T NEED THIS ANYMORE AND WE INTRODUCED FREE MOVEMENT
        # GONNA KEEP THIS HERE FOR LATER USAGE?

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.width / 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.width / 2
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def update(self):
        self.get_keys()
        self.rotation = (self.rotation + self.rotation_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rotation)
        self.rect = self.image.get_rect()
        self.hit_rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
