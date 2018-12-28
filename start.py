import pygame
from pygame.locals import *
import time
import sys
import math
import stage
import block
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

version = 'V0.0.1 beta 3'
pygame.init()

#填充背景
bgcolor=(255,217,162)
screen = pygame.display.set_mode([1920, 1280])
screen.fill(bgcolor)

#设置属性
pygame.display.set_caption("扫雷 %s" % version)
gameIcon = pygame.image.load(r"favicon.ico")
pygame.display.set_icon(gameIcon)
pygame.draw.line(screen,(0,0,0),(1042,0),(1042,1024),5)
clock = pygame.time.Clock()

#建一个group来包含要渲染的对象
mainGroup = pygame.sprite.Group()
myStage = stage.Stage()
mainGroup.add(myStage)
#初始化控制器
myStage.init()
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                x1,y1 = pygame.mouse.get_pos()
                myStage.click(x1,y1)
        else:
            x1,y1 = pygame.mouse.get_pos()
            myStage.move(x1,y1)

    clock.tick(24)
   
    # 清除游戏对象
    screen.fill(bgcolor)

    # 划线
    pygame.draw.line(screen,(0,0,0),(1027,0),(1027,1024),5)

    # 画mainGroup包含的对象
    mainGroup.draw(screen)
    mainGroup.update()

    # 刷新
    pygame.display.update()
    
    # sys.exit(0)