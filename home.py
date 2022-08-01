import pygame

pygame.init()

# Colors
BLACK = (0,0,0)
GRAY = (166,166,166)

# Fonts
font_50 = pygame.font.Font('font/Anson-Regular.otf', 50)
font_25 = pygame.font.Font('font/Anson-Regular.otf', 25)

class Home():
    def __init__(self, homeWindowSize):
        self.homeWindowSize = homeWindowSize

    def initialize(self):
        window = pygame.display.set_mode(self.homeWindowSize)
        window.fill(GRAY)
        # Title Minesweeper
        titleText = font_50.render('Minesweeper', True, BLACK)
        titleRect = titleText.get_rect(center = (self.homeWindowSize[0] / 2 , 100))
        window.blit(titleText, titleRect)
        # Beginner container
        pygame.draw.rect(window, BLACK, pygame.Rect(150, 200, 200, 50), 1, 7)
        begSizeText = font_25.render('9x9', True, BLACK)
        begSizeRect = begSizeText.get_rect(center=(250,223))
        window.blit(begSizeText, begSizeRect)
        # Intermediate container
        pygame.draw.rect(window, BLACK, pygame.Rect(150, 275, 200, 50), 1, 7)
        intSizeText = font_25.render('16x16', True, BLACK)
        intSizeRect = intSizeText.get_rect(center=(250,300))
        window.blit(intSizeText, intSizeRect)
        # Expert container
        pygame.draw.rect(window, BLACK, pygame.Rect(150, 350, 200, 50), 1, 7)
        expSizeText = font_25.render('30x16', True, BLACK)
        expSizeRect = expSizeText.get_rect(center=(250,375))
        window.blit(expSizeText, expSizeRect)

        self.run()

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    run = False
            pygame.display.flip()
        pygame.quit()