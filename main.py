import sys
from turtle import right
import numpy as np
import pygame
import random

size = 9
count = 0

pygame.init()
window = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Minesweeper')
pygame.font.init()
font_250 = pygame.font.Font('font/Anson-Regular.otf', 250)
font_120 = pygame.font.Font('font/Anson-Regular.otf', 120)
font_50 = pygame.font.Font('font/Anson-Regular.otf', 50)
font_25 = pygame.font.Font('font/Anson-Regular.otf', 25)

GRAY = (166,166,166)
DARK_GREY = (80,80,80)
BLACK = (0,0,0)

#---------- MAKING THE GAME FIELD ----------#
def defineBomb(x, y):
  if(field[x][y] == 0):
    field[x][y] = -1
  else:
    defineBomb(random.randint(0,size-1), random.randint(0,size-1))

field = np.zeros((size,size), dtype=np.int8)

if(size == 9):
  for i in range(10):
    defineBomb(random.randint(0,size-1), random.randint(0,size-1))
elif(size == 16):
  for i in range(40):
    defineBomb(random.randint(0,size-1), random.randint(0,size-1))
elif(size == 30):
  for i in range(150):
    defineBomb(random.randint(0,size-1), random.randint(0,size-1))

for i in range(size):
  for j in range(size):
    if(field[i][j] != -1):
      if(i != 0 and j != 0 and i != size-1 and j != size-1):
        if(field[i-1][j-1] == -1):
          count += 1
        if(field[i][j-1] == -1):
          count += 1
        if(field[i+1][j-1] == -1):
          count += 1
        if(field[i-1][j] == -1):
          count += 1
        if(field[i+1][j] == -1):
          count += 1
        if(field[i-1][j+1] == -1):
          count += 1
        if(field[i][j+1] == -1):
          count += 1
        if(field[i+1][j+1] == -1):
          count += 1

        field[i][j] = count
        count = 0
        
      elif(i == 0 and j == 0):
        if(field[i][j+1] == -1):
          count += 1
        if(field[i+1][j+1] == -1):
          count += 1
        if(field[i+1][j] == -1):
          count += 1

        field[i][j] = count
        count = 0

      elif(i == 0 and j == size-1):
        if(field[i][j-1] == -1):
          count += 1
        if(field[i+1][j-1] == -1):
          count += 1
        if(field[i+1][j] == -1):
          count += 1

        field[i][j] = count
        count = 0
        
      elif(i == size-1 and j == 0):
        if(field[i-1][j] == -1):
          count += 1
        if(field[i-1][j+1] == -1):
          count += 1
        if(field[i][j+1] == -1):
          count += 1

        field[i][j] = count
        count = 0
        
      elif(i == size-1 and j == size-1):
        if(field[i-1][j] == -1):
          count += 1
        if(field[i-1][j-1] == -1):
          count += 1
        if(field[i][j-1] == -1):
          count += 1

        field[i][j] = count
        count = 0
        
      elif(i == 0):
        if(field[i][j-1] == -1):
          count += 1
        if(field[i+1][j-1] == -1):
          count += 1
        if(field[i+1][j] == -1):
          count += 1
        if(field[i+1][j+1] == -1):
          count += 1
        if(field[i][j+1] == -1):
          count += 1

        field[i][j] = count
        count = 0

      elif(i == size-1):
        if(field[i][j-1] == -1):
          count += 1
        if(field[i-1][j-1] == -1):
          count += 1
        if(field[i-1][j] == -1):
          count += 1
        if(field[i-1][j+1] == -1):
          count += 1
        if(field[i][j+1] == -1):
          count += 1

        field[i][j] = count
        count = 0

      elif(j == 0):
        if(field[i-1][j] == -1):
          count += 1
        if(field[i-1][j+1] == -1):
          count += 1
        if(field[i][j+1] == -1):
          count += 1
        if(field[i+1][j+1] == -1):
          count += 1
        if(field[i+1][j] == -1):
          count += 1

        field[i][j] = count
        count = 0

      elif(j == size-1):
        if(field[i-1][j] == -1):
          count += 1
        if(field[i-1][j-1] == -1):
          count += 1
        if(field[i][j-1] == -1):
          count += 1
        if(field[i+1][j-1] == -1):
          count += 1
        if(field[i+1][j] == -1):
          count += 1

        field[i][j] = count
        count = 0
#---------- END OF MAKING THE GAME FIELD ----------#

def start():
  run = True

  flag_img = pygame.image.load('images/flag.png')
  flag_img = pygame.transform.scale(flag_img,(182,182))

  title_text = font_250.render('MineSweeper', True, BLACK)
  escape_text = font_25.render('Press ESC to quit', True, BLACK)
  beg_text = font_50.render('Beginner', True, BLACK)
  begSize_text = font_120.render('9x9', True, BLACK)
  int_text = font_50.render('Intermediate', True, BLACK)
  intSize_text = font_120.render('16x16', True, BLACK)
  exp_text = font_50.render('Expert', True, BLACK)
  expSize_text = font_120.render('30x30', True, BLACK)

  escape_rect = escape_text.get_rect(center=(1920 / 2, 1020))
  title_rect = title_text.get_rect(center=(1920 / 1.8,190))
  beg_rect = beg_text.get_rect(center=(475,495))
  begSize_rect = begSize_text.get_rect(center=(475,642))
  int_rect = int_text.get_rect(center=(960,495))
  intSize_rect = intSize_text.get_rect(center=(960,642))
  exp_rect = exp_text.get_rect(center=(1445,495))
  expSize_rect = expSize_text.get_rect(center=(1445,642))

  flag_rect = flag_img.get_rect(center=(1920 / 5.5, 200))

  window.fill(GRAY)
  window.blit(flag_img, flag_rect)
  window.blit(title_text, title_rect)
  window.blit(beg_text,beg_rect)
  window.blit(begSize_text,begSize_rect)
  window.blit(int_text,int_rect)
  window.blit(intSize_text,intSize_rect)
  window.blit(exp_text,exp_rect)
  window.blit(expSize_text,expSize_rect)
  window.blit(escape_text,escape_rect)

  pygame.draw.rect(window, BLACK, pygame.Rect(287,455,375,375), 3, 30)
  pygame.draw.rect(window, BLACK, pygame.Rect(772,455,375,375), 3, 30)
  pygame.draw.rect(window, BLACK, pygame.Rect(1257,455,375,375), 3, 30)

  pygame.display.flip()

  while(run):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          run = False
          pygame.quit()
          sys.exit()


start() 