import pygame
import block
import bomb
import random
# coding : UTF-8
class Stage(pygame.sprite.Sprite):
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
    step = 1
    radarNum = 1
    blockList = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'empty.gif')
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
    
    def init(self):
        for x in range(8):
            for y in range(8):
                # print(not blocksState[x][y] & 0x10 == 0)
                self.groups()[0].add(block.Block(self.getPosX(x), self.getPosY(y)))
        self.redBomb = bomb.Bomb('red', 1200, 200)
        self.blackBomb = bomb.Bomb('black', 1200, 200)
        self.groups()[0].add(self.blackBomb)

    def getPosX(self, pos):
        if pos > 8:
            return 8
        else:
            return pos*126+18
    def getPosY(self, pos):
        if pos > 8:
            return 8
        else:
            return pos*126+18
    def getBlockXByPos(self,pos):
        return int((pos-18)/126)
    def getBlockYByPos(self,pos):
        return int((pos-18)/126)
    def getBombPosX(self, pos):
        return pos*126+48
    def getBombPosY(self, pos):
        return pos*126+25
        
    def update(self):
        pass
    def move(self, x, y):
        if self.step == 1:
            self.blackBomb.setPos(x,y)
    def click(self, x, y):
        if self.step == 1:
            self.initLevelTwo(x, y)
        elif self.step==2:
            pass
        elif self.step == 3:
            pass
    def initLevelTwo(self, x, y):
        print(x,y)
        redX = (random.randint(0,7))
        redY = (random.randint(0,7))
        blackX = self.getBlockXByPos(x)
        blackY = self.getBlockYByPos(y)
        self.putBBomb(self.getBombPosX(blackX), self.getBombPosY(blackY))
        self.putRBomb(self.getBombPosX(redX), self.getBombPosY(redY))
        self.blocksState[blackX][blackY] = self.blocksState[blackX][blackY] | 0x01
        self.blocksState[redX][redY] = self.blocksState[redX][redY] | 0x02
        print(self.blocksState)
        self.step = 2
    def putBBomb(self, x, y):
        self.blackBomb.setPos(x, y)
    def putRBomb(self, x, y):
        self.redBomb.setPos(x, y)
        self.redBomb.hide()