import pygame
class Over(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'empty.gif')
        self.rect = self.image.get_rect()
        self.rect.topleft = [577, 425]
    def win(self):
        self.image = pygame.image.load(r'gif\win.gif')
    def loose(self):
        self.image = pygame.image.load(r'gif\loose.gif')