import pygame
class Bomb(pygame.sprite.Sprite):
    def __init__(self,color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.isHidden = True
        self.color = color
        self.image = pygame.image.load(r'empty.gif')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    def update(self):
        if self.isHidden:
            if(self.color == 'red'):
                self.image = pygame.image.load(r'gif\bomb-r.gif')
            else:
                self.image = pygame.image.load(r'gif\bomb-b.gif')
        else:
            self.image = pygame.image.load(r'empty.gif')
    def show(self):
        self.isHidden = False
    def hide(self):
        self.isHidden = True
    def setPos(self, x,y):
        self.rect.topleft = [x,y]
        

