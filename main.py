import sys, pygame, random
import numpy as np
import beginner
import intermediate
import expert

field9 = np.zeros((9,9), dtype=np.int8)
field16 = np.zeros((16,16), dtype=np.int8)
field30 = np.zeros((30,30), dtype=np.int8)

pygame.init()
window = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Minesweeper')
pygame.font.init()
font_250 = pygame.font.Font('font/Anson-Regular.otf', 250)
font_120 = pygame.font.Font('font/Anson-Regular.otf', 120)
font_50 = pygame.font.Font('font/Anson-Regular.otf', 50)
font_25 = pygame.font.Font('font/Anson-Regular.otf', 25)

GRAY = (166,166,166)
DARK_GRAY = (80,80,80)
BLACK = (0,0,0)

#---------- MAKING THE GAME FIELD ----------#
def makeField(sz):
  size = int(sz)
  count = 0

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

  return field
#---------- END OF MAKING THE GAME FIELD ----------#

#---------- COLORIZE WHEN MOUSE IS ABOVE THE CONTAINER ----------#
def colorRect(pos):
  if(pos == 1):
    pygame.draw.rect(window, DARK_GRAY, pygame.Rect(287,455,375,375), 0, 30)
    pygame.draw.rect(window, BLACK, pygame.Rect(287,455,375,375), 3, 30)
    beg_text = font_50.render('Beginner', True, BLACK)
    begSize_text = font_120.render('9x9', True, BLACK)
    beg_rect = beg_text.get_rect(center=(475,495))
    begSize_rect = begSize_text.get_rect(center=(475,642))
    window.blit(beg_text,beg_rect)
    window.blit(begSize_text,begSize_rect)

  elif(pos == 2):
    pygame.draw.rect(window, DARK_GRAY, pygame.Rect(772,455,375,375), 0, 30)
    pygame.draw.rect(window, BLACK, pygame.Rect(772,455,375,375), 3, 30)
    int_text = font_50.render('Intermediate', True, BLACK)
    intSize_text = font_120.render('16x16', True, BLACK)
    int_rect = int_text.get_rect(center=(960,495))
    intSize_rect = intSize_text.get_rect(center=(960,642))
    window.blit(int_text,int_rect)
    window.blit(intSize_text,intSize_rect)

  elif(pos == 3):
    pygame.draw.rect(window, DARK_GRAY, pygame.Rect(1257,455,375,375), 0, 30)
    pygame.draw.rect(window, BLACK, pygame.Rect(1257,455,375,375), 3, 30)
    exp_text = font_50.render('Expert', True, BLACK)
    expSize_text = font_120.render('30x30', True, BLACK)
    exp_rect = exp_text.get_rect(center=(1445,495))
    expSize_rect = expSize_text.get_rect(center=(1445,642))
    window.blit(exp_text,exp_rect)
    window.blit(expSize_text,expSize_rect)

  pygame.display.flip()
#---------- END OF COLORIZE WHEN MOUSE IS ABOVE THE CONTAINER ----------#

#---------- MAIN (start) ----------#
def start():
  run = True

  window.fill(GRAY)
  #flag image
  flag_img = pygame.image.load('images/flag.png')
  flag_img = pygame.transform.scale(flag_img,(182,182))
  flag_rect = flag_img.get_rect(center=(1920 / 5.5, 200))
  window.blit(flag_img, flag_rect)
  #title and esc for quit
  title_text = font_250.render('MineSweeper', True, BLACK)
  escape_text = font_25.render('Press ESC to quit', True, BLACK)
  escape_rect = escape_text.get_rect(center=(1920 / 2, 1020))
  title_rect = title_text.get_rect(center=(1920 / 1.8,190))
  window.blit(title_text, title_rect)
  window.blit(escape_text,escape_rect)
  #beginner container
  pygame.draw.rect(window, BLACK, pygame.Rect(287,455,375,375), 3, 30)
  beg_text = font_50.render('Beginner', True, BLACK)
  begSize_text = font_120.render('9x9', True, BLACK)
  beg_rect = beg_text.get_rect(center=(475,495))
  begSize_rect = begSize_text.get_rect(center=(475,642))
  window.blit(beg_text,beg_rect)
  window.blit(begSize_text,begSize_rect)
  #intermediate container
  pygame.draw.rect(window, BLACK, pygame.Rect(772,455,375,375), 3, 30)
  int_text = font_50.render('Intermediate', True, BLACK)
  intSize_text = font_120.render('16x16', True, BLACK)
  int_rect = int_text.get_rect(center=(960,495))
  intSize_rect = intSize_text.get_rect(center=(960,642))
  window.blit(int_text,int_rect)
  window.blit(intSize_text,intSize_rect)
  #expert container
  pygame.draw.rect(window, BLACK, pygame.Rect(1257,455,375,375), 3, 30)
  exp_text = font_50.render('Expert', True, BLACK)
  expSize_text = font_120.render('30x30', True, BLACK)
  exp_rect = exp_text.get_rect(center=(1445,495))
  expSize_rect = expSize_text.get_rect(center=(1445,642))
  window.blit(exp_text,exp_rect)
  window.blit(expSize_text,expSize_rect)

  pygame.display.flip()

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
    
      mouseX, mouseY = pygame.mouse.get_pos()
      if((mouseX >= 287 and mouseX <= 662) and (mouseY >= 455 and mouseY <= 830)):
        colorRect(1)
        if event.type == pygame.MOUSEBUTTONUP:
          field9 = makeField(9)
          beginner.beginnerGame(field9)
      else:
        pygame.draw.rect(window, GRAY, pygame.Rect(287,455,375,375), 0, 30)
        pygame.draw.rect(window, BLACK, pygame.Rect(287,455,375,375), 3, 30)
        window.blit(beg_text,beg_rect)
        window.blit(begSize_text,begSize_rect)

      if((mouseX >= 772 and mouseX <= 1147) and (mouseY >= 455 and mouseY <= 830)):
        colorRect(2)
        if event.type == pygame.MOUSEBUTTONUP:
          field16 = makeField(16)
          intermediate.intermediateGame(field16)
      else:
        pygame.draw.rect(window, GRAY, pygame.Rect(772,455,375,375), 0, 30)
        pygame.draw.rect(window, BLACK, pygame.Rect(772,455,375,375), 3, 30)
        window.blit(int_text,int_rect)
        window.blit(intSize_text,intSize_rect)

      if((mouseX >= 1257 and mouseX <= 1632) and (mouseY >= 455 and mouseY <= 830)):
        colorRect(3)
        if event.type == pygame.MOUSEBUTTONUP:
          field30 = makeField(30)
          expert.expertGame(field30)
      else:
        pygame.draw.rect(window, GRAY, pygame.Rect(1257,455,375,375), 0, 30)
        pygame.draw.rect(window, BLACK, pygame.Rect(1257,455,375,375), 3, 30)
        window.blit(exp_text,exp_rect)
        window.blit(expSize_text,expSize_rect)

      pygame.display.flip()
#---------- END OF MAIN ----------#

start() 