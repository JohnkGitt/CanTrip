import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('PSprites.png')

        #16x26
        self.sheet.set_clip(pygame.Rect(0, 0, 16, 26))

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        self.rect.topleft = position

        self.leftWalkStates = {0:(0, 0, 16, 26), 1:(16, 0, 16, 26), 2:(32, 0, 16, 26), 3:(48, 0, 16, 26),
                               4:(64, 0, 16, 26), 5:(80, 0, 16, 26), 6:(128, 0, 16, 26), 7:(144, 0, 32, 26)}

        self.rightWalkStates = {0:(192, 20, 16, 26), 1:(176, 20, 16, 26), 2:(160, 20, 16, 26), 3:(144, 20, 16, 26),
                                4:(128, 20, 16, 26), 5:(112, 20, 16, 26), 6:(96,20, 16, 26), 7:(80, 20, 16, 26)}
