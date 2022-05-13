import numpy as np
import pygame
import random

size = int(input())
count = 0

pygame.init()
window = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Minesweeper')
pygame.font.init()


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

print(field)