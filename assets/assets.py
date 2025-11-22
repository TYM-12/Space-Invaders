import pygame
from .loader import load_image
from config import width, height
class Assets:
    def __init__(self):
        self.player = load_image("assets/player.png", (64, 64))
        self.laser = load_image("assets/laser.png", (16, 32))
        self.alien = load_image("assets/alien.png", (48, 48))
        self.background = load_image("assets/background.jpg", (width, height))