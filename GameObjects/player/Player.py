import pygame
import os
from GameObjects.GameObjects import gameObject
from enum import Enum
from GameObjects.Att_Block.Att_Block import Att_Block
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.GameObjects import RESOURCES_FILEPATH


RESOURCES_FILEPATH = os.path.join('Resources', '')


class PlayerAttributes(Enum):
    JUMP = 0
    WALK_LEFT = 1
    WALK_RIGHT = 2
    GRAB = 3

class Player(gameObject):
    def __init__(self, x, y, width, height, id):
        super().__init__(x, y, width, height, id)
        self.ID = id
        self.lastFace = ''
        self.sheet = pygame.image.load(f'{RESOURCES_FILEPATH}PSprites_scaled2x.png')
        self.width = width
        self.height = height
        self.finalx = 0
        self.finaly = 0

        self.grabbed = []

        #16x26
        self.sheet.set_clip(pygame.Rect(0, 0, 32, 52))

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        self.rect.topleft = (x, y)

        self.frame = 0

        self.leftWalkStates = {7:(0, 0, 32, 52), 6:(32, 0, 32, 52), 5:(64, 0, 32, 52), 4:(96, 0, 32, 53),
                               3:(128, 0, 32, 52), 2:(160, 0, 32, 52), 1:(192, 0, 32, 52), 0:(224, 0, 32, 52)}

        self.rightWalkStates = {7:(384, 62, 32, 52), 6:(352, 62, 32, 52), 5:(320, 62, 32, 52), 4:(288, 62, 32, 52),
                                3:(256, 62, 32, 52), 2:(224, 62, 32, 52), 1:(192, 62, 32, 52), 0:(160, 62, 32, 52)}

        self.leftIdleStates = {0:(288, 0, 32, 52), 1:(320, 0, 32, 52), 2:(352, 0, 32, 52), 3:(384, 0, 32, 52)}

        self.rightIdleStates = {0:(0, 62, 32, 52), 1:(32, 62, 32, 52), 2:(64, 62, 32, 52), 3:(96, 62, 32, 52)}

        self.leftJump = {0:(0, 0, 32, 52)}
        self.rightJump = {0: (384, 62, 32, 52)}

        self.isJumping = False
        self.jumpCount = 0

        self.jumpSound = pygame.mixer.Sound(f'{RESOURCES_FILEPATH}jump.mp3')
        self.grabSound = pygame.mixer.Sound(f'{RESOURCES_FILEPATH}grab.mp3')
        self.placeSound = pygame.mixer.Sound(f'{RESOURCES_FILEPATH}place.mp3')

    def get_frame(self, frame_set):
            self.frame += 1
            if self.frame > (len(frame_set) - 1):
                self.frame = 0

            return frame_set[self.frame]

    def clip(self, clipped_rect):
            if type(clipped_rect) is dict:
                self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
            else:
                self.sheet.set_clip(pygame.Rect(clipped_rect))
            return clipped_rect

    def update(self, direction, collideList):
            finalx = self.rect.x
            finaly = self.rect.y

            if not self.onGround(collideList):
                self.rect.y += 5
            if self.isJumping:
                if self.jumpCount == 20:
                    self.jumpCount = 0
                    self.isJumping = False
                if self.jumpCount > 14:
                    self.jumpCount += 1
                    self.rect.y -= 12
                else:
                    self.jumpCount += 1
                    self.rect.y -= 15
            if direction == 'left':
                self.clip(self.leftWalkStates)
                self.rect.x -= self.left_collide(collideList)
                self.lastFace = 'left'
            if direction == 'right':
                self.clip(self.rightWalkStates)
                self.rect.x += self.right_collide(collideList)
                self.lastFace = 'right'
            if direction == 'stand_left':
                self.clip(self.leftIdleStates)
            if direction == 'stand_right':
                self.clip(self.rightIdleStates)
            if direction == 'up':
                self.jump(collideList)
            finalx = finalx - self.rect.x
            finaly = finaly - self.rect.y

            if len(self.grabbed) > 0:
                self.grabbed[0].update2(finalx, finaly)

            self.image = self.sheet.subsurface(self.sheet.get_clip())

    def onGround(self, collideList):
        for sprite in collideList:
            if self.rect.colliderect(sprite.rect):
                return True
        return False

    def left_collide(self, collideList):
        count = 0
        for sprite in collideList:
            if count > 0:
                dif =   self.rect.left - sprite.rect.right
                cond1 = 5 > dif >= 0
                cond2 = self.rect.bottom > sprite.rect.top  and sprite.rect.bottom >  self.rect.top
                if cond1 and cond2:
                    return dif
            count+=1
        return 5

    def right_collide(self, collideList):
        count = 0
        for sprite in collideList:
            if count > 0:
                dif = sprite.rect.left - self.rect.right
                cond1 = 5 > dif >= 0
                cond2 = self.rect.bottom > sprite.rect.top and sprite.rect.bottom > self.rect.top
                if cond1 and cond2:
                    return dif
            count += 1
        return 5

    def jump(self, collideList):
        if not(self.isJumping) and self.onGround(collideList):
            self.isJumping = True
            self.jumpSound.play()


    def getID(self):
        return self.ID

    def setPOS(self, X, Y):
        self.rect.x = X
        self.rect.y = Y

    def getPOS(self):
        return self.rect.x, self.rect.y

    def att_Handler(self):
        pass

    def getDelta(self):
        return self.finalx, self.finaly

    def grab(self, blockGroup, collideGroup):
        self.grabSound.play()
        if self.lastFace == 'left':
            self.grabCollider = pygame.Rect(self.rect.x - 20, self.rect.y, 20, self.rect.height)
            for block  in blockGroup:
                if self.grabCollider.colliderect(block):
                    self.grabbed.append(block)
                    block.rect.y -= self.rect.height
                    block.rect.x = self.rect.x - self.rect.width
                    collideGroup.remove(block)
                    self.grabbed[0].changeGrabbed()
                    return
        else:
            self.grabCollider = pygame.Rect(self.rect.right + 20, self.rect.y, 20, self.rect.height)
            for block in blockGroup:
                if self.grabCollider.colliderect(block):
                    self.grabbed.append(block)
                    block.rect.y -= self.rect.height
                    block.rect.x = self.rect.x - self.rect.width
                    collideGroup.remove(block)
                    self.grabbed[0].changeGrabbed()
                    return

    def place(self, collideList):
        if self.lastFace == 'left':
            self.grabbed[0].rect.x = self.rect.left - 10 - self.grabbed[0].rect.width
        elif self.lastFace == 'right':
            self.grabbed[0].rect.x = self.rect.right + 10
        self.grabbed[0].rect.bottom = self.rect.bottom - 9
        self.grabbed[0].collide_adjust(collideList)
        collideList.add(self.grabbed[0])
        self.grabbed[0].changeGrabbed()
        self.grabbed.pop()
        self.placeSound.play()

    def getID(self):
        return self.ID

