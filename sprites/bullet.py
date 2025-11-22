import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        super().__init__()
        self.image = assets.laser
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10
    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()