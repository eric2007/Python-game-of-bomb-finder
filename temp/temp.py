x,y = pygame.mouse.get_pos()
        if radarNum == (self.num) *2 -1 and step == 2:
            self.rect.topleft = [x-39,y-50]
        if radarNum == (self.num) *2 +1 and step == 2:
            if pygame.mouse.get_pressed() == (1,0,0):
                if (x - 18) % 126 < 120 and (y - 18) % 126 <120 and x < 1024:
                    x1,y1 = pygame.mouse.get_pos()
                    x2 = x1 - 18
                    y2 = y1 - 18
                    pathX = int(math.floor(x2 / 126))
                    pathY = int(math.floor(y2 / 126))
                    blocksState[pathX][pathY] = blocksState[pathX][pathY] | 0x04
                    pygame.mouse.set_visible(True)
                    self.rect.topleft = [pathX*126+39,pathY*126+28]
                    n = 0
                    if blocksState[pathX][pathY] & 0x02 != 0:
                        n += 1
                    if blocksState[pathX - 1][pathY] & 0x02 != 0:
                        n += 1
                    if blocksState[pathX + 1][pathY] & 0x02 != 0:
                        n += 1
                    if blocksState[pathX][pathY - 1] & 0x02 != 0:
                        n += 1
                    if blocksState[pathX][pathY + 1] & 0x02 != 0:
                        n += 1
                    blitText(str(n),pathX,pathY,(0,0,0))