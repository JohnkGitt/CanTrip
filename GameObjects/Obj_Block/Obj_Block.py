import pygame
from GameObjects.GameObjects import gameObject
from GameObjects.GameObjects import RESOURCES_FILEPATH

class Obj_Block(gameObject):
    def __init__(self, x, y, width, height, id, text, target, has_physics=True, grabbable=True):
        self.has_physics = has_physics
        self.grabbable = grabbable
        super().__init__(x, y, width, height, id, has_physics=has_physics, grabbable=grabbable)
        self.text = text
        self.target = target
        if text == "Door":
            self.sheet = pygame.image.load(f'{RESOURCES_FILEPATH}DoorBlock.png')
        elif text == "CANRobot":
            self.sheet = pygame.image.load(f'{RESOURCES_FILEPATH}BotBlock.jpg')
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

    def update(self, collideList):
        self.fall(collideList)

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

    def getTargetID(self):
        return self.target


