class Radar(pygame.sprite.Sprite):
    def __init__(self,num, color):
        pygame.sprite.Sprite.__init__(self)
        if color == 'red':
            self.image = pygame.image.load(r'gif\radar-r.gif')
        else:
            self.image = pygame.image.load(r'gif\radar-b.gif')
        self.rect = self.image.get_rect()
        x = num * 106 + 1026
        self.rect.topleft = [x,0]
        self.num = num
    def update(self):
        pass