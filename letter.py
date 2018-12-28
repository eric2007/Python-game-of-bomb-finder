class letter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        font = pygame.font.SysFont('arial',30)
        self.image = font.render('string',True,(0,0,0))
        self.rect = self.image.get_rect()
        x = 1 * 126 + 33
        y = 1 * 126 + 100
        self.rect.topleft = [x,y]