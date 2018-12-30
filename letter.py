import pygame
class letter(pygame.sprite.Sprite):
    def __init__(self, x, y, string, color):
        pygame.sprite.Sprite.__init__(self)
        font = pygame.font.Font('font.ttf',30)
        self.image = font.render(string,True,color)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    def update(self):
        pass