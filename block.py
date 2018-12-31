import pygame
class Block(pygame.sprite.Sprite):
    def __init__(self,pos_X,pos_Y):
        pygame.sprite.Sprite.__init__(self)       
        self.x = pos_X
        self.y = pos_Y
        self.isHidden = False
        self.image = pygame.image.load(r'gif\brick.gif')
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]
    def update(self):
        if self.isHidden:
            self.image = pygame.image.load(r'empty.gif')
    def hide(self):
        print('hide')
        self.isHidden = True