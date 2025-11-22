import pygame
from config import width,height
import random
class Alien(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        super().__init__()
        self.image = assets.alien
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = random.randint(2, 5)
    def update(self, *args):
        self.rect.y += self.speed_y
        if self.rect.top > height:
            self.kill()