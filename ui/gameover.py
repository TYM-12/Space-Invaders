import pygame
from config import width,height
def game_over_screen(screen, font, score):
    screen.fill((0, 0, 0))
    over_text = font.render("GAME OVER", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    info_text = font.render("Press any key to quit", True, (255, 255, 255))

    rect = over_text.get_rect(center=(width//2, height//2-20))
    srect = score_text.get_rect(center=(width//2, height//2+20))
    irect = info_text.get_rect(center=(width//2, height//2+60))

    screen.blit(over_text, rect)
    screen.blit(score_text, srect)
    screen.blit(info_text, irect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN:
                waiting = False