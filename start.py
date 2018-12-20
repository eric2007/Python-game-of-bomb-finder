import pygame
from pygame.locals import *
import time
# from pygame.locals import *
import sys
import random, os.path
# try:
#     import pygame.freetype as freetype
# except ImportError:
#     print ("No FreeType support compiled")
#     raise SystemExit("Sorry, extended image module required")
# pygame.init()
#     
# block(0,1) 
#   ↘  ↓   ↙
# 0b 0 00 00
blocksState = [
    [0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,],
    [0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,],
    [0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,],
    [0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,],
    [0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,],
    [0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,],
    [0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,],
    [0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,],
]
version = '0.0.1 beta 1'
class block(pygame.sprite.Sprite):
    def __init__(self,pos_X,pos_Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'gif\brick.gif')
        self.rect = self.image.get_rect()
        self.x = pos_X
        self.y = pos_Y
        self.rect.topleft = [pos_X*126+20,pos_Y*126+20]
    def update(self):
        pass
screen = pygame.display.set_mode([1920, 1280])
screen.fill((255,217,162))
pygame.display.set_caption("扫雷 V%s" % version)
group = pygame.sprite.Group()
for x in range(8):
        for y in range(8):
            # print(not blocksState[x][y] & 0x10 == 0)
            if not blocksState[x][y] & 0x10 == 0:
                group.add(block(x,y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()
    # font = pygame.font.SysFont('Arial',32)
    # textFrame = font.render("Hello world!", True, GREEN)
    # frame = textFrame.get_rect()
    # frame.center=(400,300)
    # DISPLAYSURF.blit(textFrame,frame)
    pygame.display.update()
    group.update()
    group.draw(screen)
    pygame.display.update()
    
pygame.display.update()
    # sys.exit(0)