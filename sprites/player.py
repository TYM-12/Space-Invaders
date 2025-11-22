
import pygame
from config import width,height

class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        super().__init__()
        self.image = assets.player
        self.rect = self.image.get_rect()
        self.rect.centerx = width//2
        self.rect.bottom = height-20
        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width