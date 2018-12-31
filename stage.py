import pygame
import block
import bomb
import radar
import random
import letter
import over
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
    radarNum = 0
    blackRadar = []
    redRadar = []
    blocks = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'empty.gif')
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
    def init(self):
        for x in range(8):
            temp = []
            for y in range(8):
                # print(not blocksState[x][y] & 0x10 == 0)
                temp.append(block.Block(self.getPosX(x), self.getPosY(y)))
            self.blocks.append(temp)
        for x in range(8):
            for y in range(8):
                # print(not blodcksState[x][y] & 0x10 == 0)
                self.groups()[0].add(self.blocks[x][y])
        self.redBomb = bomb.Bomb('red', 1200, 200)
        self.blackBomb = bomb.Bomb('black', 1200, 200)
        self.blackBomb.show()
        self.redBomb.setPos(1729, 18)
        self.groups()[0].add(self.blackBomb)
        self.board = over.Over()
        self.groups()[0].add(self.board)
        for _ in range(3):
            self.blackRadar.append(radar.Radar('black'))
        for _ in range(3):
            self.redRadar.append(radar.Radar('red'))
        for n in range(3):
            self.groups()[0].add(self.blackRadar[n])
            self.blackRadar[n].setPos(18, n * 106 + 18)
        for n in range(3):
            self.groups()[0].add(self.redRadar[n])
            self.redRadar[n].setPos(1814, n * 106 + 18)
        pygame.mouse.set_visible(False)
    # 447 18
    def getPosX(self, pos):
        return pos*126+465
    def getPosY(self, pos):
        return pos*126+18
    def getBlockXByPos(self,pos):
        return int((pos-465)/126)
    def getBlockYByPos(self,pos):
        return int((pos-18)/126)
    def getBombPosX(self, pos):
        return pos*126+477
    def getBombPosY(self, pos):
        return pos*126+28
    def getRadarPosX(self, pos):
        return pos*126+457
    def getRadarPosY(self, pos):
        return pos*126+28
    def update(self):
        pass
    def move(self, x, y):
        if self.step == 1:
            self.blackBomb.setPos(x - 49,y - 50)
        elif self.step == 2:
            self.blackRadar[self.radarNum].setPos(x - 50, y - 50)
    def click(self, x, y):
        if self.step == 1:
            self.initLevelTwo(x, y)
        elif self.step==2:
            self.putRadar(x, y, self.radarNum)
        elif self.step == 3:
            self.dig(x, y)
    def initLevelTwo(self, x, y):
        # print(x,y)
        redX = (random.randint(0,7))
        redY = (random.randint(0,7))
        blackX = self.getBlockXByPos(x)
        blackY = self.getBlockYByPos(y)
        if blackX <= 7 and blackX >= 0 and blackY <= 7:
            self.putBlackBomb(self.getBombPosX(blackX), self.getBombPosY(blackY))
            self.putRedBomb(self.getBombPosX(redX), self.getBombPosY(redY))
            # pygame.mouse.set_visible(True)
            self.blocksState[blackX][blackY] = self.blocksState[blackX][blackY] | 0x01
            self.blocksState[redX][redY] = self.blocksState[redX][redY] | 0x02
            self.printList()
            self.step = 2
    def putRadar(self, x, y, num):
        # print(x,y)
        redX = (random.randint(0,7))
        redY = (random.randint(0,7))
        blackX = self.getBlockXByPos(x)
        blackY = self.getBlockYByPos(y)
        if blackX <= 7 and blackX >= 0 and blackY <= 7:
            self.putBlackRadar(self.getRadarPosX(blackX), self.getRadarPosY(blackY), blackX, blackY, num)
            self.putRedRadar(self.getRadarPosX(redX), self.getRadarPosY(redY), redX, redY, num)
            self.blocksState[blackX][blackY] = self.blocksState[blackX][blackY] | 0x04
            self.blocksState[redX][redY] = self.blocksState[redX][redY] | 0x08
            if num == 2:
                print(self.blocksState)
                self.step = 3
                self.initLevelThree()
            else:
                self.radarNum += 1
    def win(self):
        self.groups()[0].add()
    def initLevelThree(self):
        pygame.mouse.set_visible(True)
    def dig(self, x, y):
        posX = self.getBlockXByPos(x)
        posY = self.getBlockYByPos(y)
        self.digBlock(posX, posY)
        if self.blocksState[posX][posY] & 0x02 != 0:
            self.redBomb.show()
            self.board.win()
        self.digBlock(random.randint(0,7), random.randint(0,7))
        if self.blocksState[posX][posY] & 0x01 != 0:
            self.board.loose()
    def printList(self):
        for m in self.blocksState:
            for n in m:
                print(n,end = ',')
            print()
    def putBlackBomb(self, x, y):
        self.blackBomb.setPos(x, y)
    def putRedBomb(self, x, y):
        self.redBomb.setPos(x, y)
        self.redBomb.hide()
    def digBlock(self, posX, posY):
        self.blocksState[posX][posY] = 0x0f & self.blocksState[posX][posY]
        self.blocks[posX][posY].hide()
    def putBlackRadar(self, x, y, posX, posY, num):
        self.blackRadar[num].setPos(x, y)
        n = 0
        # posX = self.getBlockXByPos(x)
        # posY = self.getBlockYByPos(y)
        print(num, x, y, 'TD0')
        # print(posX,posY,'TD1')
        # try:
        if self.blocksState[posX][posY] & 0x02 != 0:
            n += 1
        if posX != 7 and self.blocksState[posX + 1][posY] & 0x02 != 0:
            n += 1
        if posX != 0 and self.blocksState[posX - 1][posY] & 0x02 != 0:
            n += 1
        if posY != 7 and self.blocksState[posX][posY + 1] & 0x02 != 0:
            n += 1
        if posY != 0 and self.blocksState[posX][posY - 1] & 0x02 != 0:
            n += 1
        # except IndexError:
        #     print('crashed')
        self.groups()[0].add(letter.Letter(x + 80, y, str(n), (0,0,0)))
        if n:
            print('dig a bomb')
            # TODO 挖一次炸弹
    def putRedRadar(self, x, y, posX, posY, num):
        self.redRadar[num].setPos(x, y)
        n = 0
        # posX = self.getBlockXByPos(x + 50)
        # posY = self.getBlockYByPos(y + 50)
        if self.blocksState[posX][posY] & 0x01 != 0:
            n += 1
        if posX != 7 and self.blocksState[posX + 1][posY] & 0x01 != 0:
            n += 1
        if posX != 0 and self.blocksState[posX - 1][posY] & 0x01 != 0:
            n += 1
        if posY != 7 and self.blocksState[posX][posY + 1] & 0x01 != 0:
            n += 1
        if posY != 0 and self.blocksState[posX][posY - 1] & 0x01 != 0:
            n += 1
        self.groups()[0].add(letter.Letter(x + 80, y, str(n), (255,0,0)))
        if n:
            print('dig a bomb')
            # TODO 挖一次炸弹