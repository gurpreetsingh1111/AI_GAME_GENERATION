# gamemode.py
import pygame, maps
from pygame.locals import *
from loader import load_image
from random import randint

PENALTY_COOL = 180
FLAG_SCORE = 15
CRASH_PENALTY = -2
HALF_TILE = 500
FULL_TILE = 1000
COUNTDOWN_FULL = 3600
COUNTDOWN_EXTEND = 750


# This class is used as a single object, which moves around
# and keeps track of player score. It also manages the countdown timer.
class Finish(pygame.sprite.Sprite):
    # The player has collided and should pick the flag.
    def claim_flag(self):
        self.score += FLAG_SCORE
        self.timeleft += COUNTDOWN_EXTEND
        if self.timeleft > COUNTDOWN_FULL:
            self.timeleft = COUNTDOWN_FULL

    # The player has crashed into another vehicle, deduct some points.
    def car_crash(self):
        if (self.penalty_cool == 0):
            self.score += CRASH_PENALTY
            self.penalty_cool = PENALTY_COOL

    # Find an adequate point to spawn flag.
    def generate_finish(self):
        x = randint(0, 9)
        y = randint(0, 9)
        while (maps.map_1[y][x] == 5):
            x = randint(0, 9)
            y = randint(0, 9)

        self.x = x * FULL_TILE + HALF_TILE
        self.y = y * FULL_TILE + HALF_TILE
        self.rect.topleft = self.x, self.y

    # Reset the state of the timer, score and respawn the flag.
    def reset(self):
        self.timeleft = COUNTDOWN_FULL
        self.score = 0
        self.generate_finish()

    # Initialize.. yes.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('C:\\Users\\GURPREET\\PycharmProjects\\AI_GAME_GENERATION\\src\\media\\finish.png', False)
        self.rect = self.image.get_rect()
        self.x = 5
        self.y = 5
        self.penalty_cool = PENALTY_COOL
        self.generate_finish()
        self.rect.topleft = self.x, self.y
        self.score = 0
        self.timeleft = COUNTDOWN_FULL

    # Update the timer and reposition the flag by offset.
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y
        if (self.penalty_cool > 0):
            self.penalty_cool -= 1
        if (self.timeleft > 0):
            self.timeleft -= 1
