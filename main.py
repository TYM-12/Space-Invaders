"""
SPACE INVADERS QUESTION VERSION (ASSETS + SPRITES)

Student task:
Use these remarks to write the full game.

Steps:
  1. Import modules and define screen size
  2. Write image loader and Assets class
  3. Write Player, Bullet, and Alien sprite classes
  4. Write game_over_screen function
  5. Write main() game loop:
       - create window
       - create assets and sprites
       - handle input
       - spawn aliens
       - update sprites
       - check collisions
       - draw everything
       - show game over
"""

# import the pygame module

# import the sys module
import sys
sys.dont_write_bytecode = True
import pygame
# import the random module
import random
from config import width,height
from assets.assets import Assets
from sprites.player import Player
from sprites.bullet import Bullet
from sprites.alien import Alien
from ui.gameover import game_over_screen
def main():
    pygame.init()
    screen = pygame.display.set_mode((width ,height))
    pygame.display.set_caption("Spacce Invaders")
    clock = pygame.time.Clock()
    assets = Assets()
    font = pygame.font.SysFont(None, 32)
    player = Player(assets)
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    all_sprites.add(player)
    score = 0
    lives = 3
    spawn_timer = 0
    spawn_interval = random.randint(30, 60)
    running = True
    while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(assets, player.rect.centerx, player.rect.top)
                bullet2 = Bullet(assets, player.rect.x, player.rect.top)
                all_sprites.add(bullet)
                all_sprites.add(bullet2)
                bullets.add(bullet2)
                bullets.add(bullet)
        keys = pygame.key.get_pressed()
        spawn_timer+=1
        if spawn_timer>=spawn_interval:
            spawn_timer = 0
            x = random.randint(50, width-50)
            alien = Alien(assets, x, -60)
            all_sprites.add(aliens)
            aliens.add(alien)
        all_sprites.update(keys)
        hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
        if hits:
            score+=len(hits)*10
        player_hits = pygame.sprite.spritecollide(player, aliens, True)
        if player_hits:
            lives-=1
            if lives<=0:
                running=False
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        score_text = font.render(f"Score: {score}", True, (255, 0, 255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 0, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (width-120, 10))
        pygame.display.flip()
        clock.tick(60)
    game_over_screen(screen, font, score)
    pygame.quit()
    sys.exit()
if __name__=="__main__":
  main()