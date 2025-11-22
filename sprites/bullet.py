import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, x, y, angle=0):
        super().__init__()
        self.image = assets.laser       # ← FIXED HERE
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10
        self.angle = math.radians(angle)

    def update(self):
        self.rect.x += self.speed * math.sin(self.angle)
        self.rect.y -= self.speed * math.cos(self.angle)
