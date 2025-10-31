import pygame
from GameObjects.GameObjects import gameObject
from GameObjects.GameObjects import RESOURCES_FILEPATH

class Att_Block(gameObject):
    def __init__(self, x, y, width, height, id, text, attribute):
        super().__init__(x, y, width, height, id)
        self.isGrabbed = False
        self.text = text
        self.att = attribute
        self.sheet = pygame.image.load(f'{RESOURCES_FILEPATH}att_block.png')

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
                if self.rect.colliderect(sprite.rect) and self != sprite:
                    return True
            return False

    def update(self, collideList):
        if not self.onGround(collideList) and not self.isGrabbed:
            self.rect.y += 5

    def update2(self, X, Y):
            self.rect.x -= X
            self.rect.y -= Y

    def changeGrabbed(self):
        self.isGrabbed = not self.isGrabbed

    def collide_adjust(self, colliders):
        for sprite in colliders:
            if self.rect.colliderect(sprite.rect):
                ydiff = self.rect.bottom - sprite.rect.top
                ldiff = sprite.rect.right - self.rect.left
                rdiff = self.rect.right - sprite.rect.left
                if ydiff < ldiff and ydiff < rdiff:
                    self.rect.y -= ydiff
                elif ldiff > rdiff:
                    self.rect.x += ldiff
                else:
                    self.rect.x += rdiff
