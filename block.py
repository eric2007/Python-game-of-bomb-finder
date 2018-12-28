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
        pass
    def clear(self):
        self.isHidden = True