import pygame
from GameObjects.GameObjects import gameObject

class Att_Block(gameObject):
    def __init__(self, x, y, width, height, id, text, attribute):
        super().__init__(x, y, width, height, id)
        self.text = text
        self.att = attribute
        self.sheet = pygame.image.load('att_block.png')

        self.sheet.set_clip(pygame.Rect(0, 0, 80, 80))

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_text(self):
        return self.text
    
    def set_text(self, text):
        self.text = text

    def onGround(self, collideList):
            for sprite in collideList:
                if self.rect.colliderect(sprite.rect):
                    return True
            return False

    def update(self, collideList):
            if not self.onGround(collideList):
                self.rect.y += 5

    def update2(self, X, Y):
            self.rect.x += X
            self.rect.y += Y

