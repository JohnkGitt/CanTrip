import pygame
from GameObjects.GameObjects import gameObject

class Obj_Block(gameObject):
    def __init__(self, x, y, width, height, id, text, target):
        super().__init__(x, y, width, height, id)
        self.text = text
        self.target = target
        self.sheet = pygame.image.load('obj_block.png')
        self.isGrabbed = False

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
        pass

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


