import numpy as np
import pygame, sys

field = np.zeros((16,16), dtype=np.int8)

pygame.init()
window = pygame.display.set_mode((1920,1080))

GRAY = (166,166,166)
DARK_GRAY = (80,80,80)
BLACK = (0,0,0)

def intermediateGame(fd):
    run = True
    field = fd

    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()

        window.fill(BLACK)
        pygame.display.update()