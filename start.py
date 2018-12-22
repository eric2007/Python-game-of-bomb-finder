import pygame
from pygame.locals import *
import time
import sys
import random
import math
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
mousebutton = False
step = 1
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
version = '0.0.1 beta 2'
class block(pygame.sprite.Sprite):
    def __init__(self,pos_X,pos_Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'gif\brick.gif')
        self.rect = self.image.get_rect()
        self.x = pos_X
        self.y = pos_Y
        self.rect.topleft = [pos_X*126+18,pos_Y*126+18]
    def update(self):
        if blocksState[self.x][self.y] & 0x10 == 0:
            self.remove()
class bombB(pygame.sprite.Sprite):
    def __init__(self,step):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'gif\bomb-b.gif')
        self.rect = self.image.get_rect()
        x, y = pygame.mouse.get_pos()
        x -= 39
        y -= 5
        self.step = step
        self.rect.topleft = [x,y]
        pygame.mouse.set_visible(False)
    def update(self):
        if self.step == 1:
            x, y = pygame.mouse.get_pos()
            self.rect.topleft = [x-39,y-50]
            if mousebutton:
                if (x - 18) % 126 < 120 and (y - 18) % 126 <120 and x < 1024:
                    print('enter step 2')
                    self.step = 2
                    x1,y1 = pygame.mouse.get_pos()
                    x2 = x1 - 18
                    y2 = y1 - 18
                    pathX = int(math.floor(x2 / 126))
                    pathY = int(math.floor(y2 / 126))
                    blocksState[pathX][pathY] = blocksState[pathX][pathY] | 0x01
                    pygame.mouse.set_visible(True)
                    self.rect.topleft = [pathX*126+39,pathY*126+28]
        if self.step == 2:
            # x = 0
            # y = 0
            # for i in blocksState:
            #     flag = False
            #     for j in i:
            #         if j & 0x01 != 0:
            #             flag = True
            #         if flag:
            #             break
            #         y += 1
            #     if flag:
            #         break
            #     x += 1
            # print(x,y)
            pass
bgcolor=(255,217,162)
screen = pygame.display.set_mode([1920, 1280])
screen.fill(bgcolor)

# 清除游戏对象
def clear_callback(surf, rect):  # 定义清除游戏对象的方法
    surf.fill(bgcolor, rect)  # 屏幕外观中的游戏对象区域填充背景颜色

pygame.display.set_caption("扫雷 V%s" % version)
group = pygame.sprite.Group()
bomb = bombB(step)
pygame.draw.line(screen,(0,0,0),(1027,0),(1027,1024),5)
for x in range(8):
        for y in range(8):
            # print(not blocksState[x][y] & 0x10 == 0)
            group.add(block(x,y))
group.add(bomb)
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            mousebutton = True
        else:
            mousebutton = False
    # font = pygame.font.SysFont('Arial',32)
    # textFrame = font.render("Hello world!", True, GREEN)
    # frame = textFrame.get_rect()
    # frame.center=(400,300)
    # DISPLAYSURF.blit(textFrame,frame)
    group.clear(screen, clear_callback)
    group.update()
    group.draw(screen)
    pygame.display.update()
    pygame.draw.line(screen,(0,0,0),(1027,0),(1027,1024),5)
    # sys.exit(0)