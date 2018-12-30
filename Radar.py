import pygame
class Radar(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        if color == 'red':
            self.image = pygame.image.load(r'gif\radar-r.gif')
        else:
            self.image = pygame.image.load(r'gif\radar-b.gif')
        self.rect = self.image.get_rect()
    def setPos(self, x, y):
        self.rect.topleft = [x, y]
    def update(self):
        pass