import numpy as np
import pygame as pg
import random

size = 9
count = 0

def defineBomb(x, y):
  if(field[x][y] == 0):
    field[x][y] = -1
  else:
    defineBomb(random.randint(0,8), random.randint(0,8))

field = np.zeros((9,9), dtype=np.int8)

for i in range(10):
  defineBomb(random.randint(0,8), random.randint(0,8))

for i in range(size):
  for j in range(size):
    if(field[i][j] != -1):
      if(i != 0 and j != 0 and i != 8 and j != 8):
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

print(field)