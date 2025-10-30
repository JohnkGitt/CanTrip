import pygame
from GameObjects.GameObjects import gameObject
from enum import Enum
from GameObjects.Att_Block.Att_Block import Att_Block
from GameObjects.Obj_Block.Obj_Block import Obj_Block

class PlayerAttributes(Enum):
    JUMP = 0
    WALK_LEFT = 1
    WALK_RIGHT = 2
    GRAB = 3

class Player(gameObject):
    def __init__(self, x, y):
        self.ID = 1
        self.lastFace = ''
        self.sheet = pygame.image.load('PSprites.png')

        self.finalx = 0
        self.finaly = 0

        self.grabbed = []

        #16x26
        self.sheet.set_clip(pygame.Rect(0, 0, 16, 26))

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        self.rect.topleft = (x, y)

        self.frame = 0

        self.leftWalkStates = {0:(0, 0, 16, 26), 1:(16, 0, 16, 26), 2:(32, 0, 16, 26), 3:(48, 0, 16, 26),
                               4:(64, 0, 16, 26), 5:(80, 0, 16, 26), 6:(96, 0, 16, 26), 7:(112, 0, 32, 26)}

        self.rightWalkStates = {0:(192, 31, 16, 26), 1:(176, 31, 16, 26), 2:(160, 31, 16, 26), 3:(144, 31, 16, 26),
                                4:(128, 31, 16, 26), 5:(112, 31, 16, 26), 6:(96, 31, 16, 26), 7:(80, 31, 16, 26)}

        self.leftIdleStates = {0:(144, 0, 16, 26), 1:(160, 0, 16, 26), 2:(176, 0, 16, 26), 3:(192, 0, 16, 26)}

        self.rightIdleStates = {0:(48, 31, 16, 26), 1:(32, 31, 16, 26), 2:(16, 31, 16, 26), 3:(0, 31, 16, 26)}

        self.leftJump = {0:(0, 0, 16, 26)}
        self.rightJump = {0: (192, 20, 16, 26)}

        self.isJumping = False
        self.jumpCount = 0

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
                    self.rect.y -= 9
                else:
                    self.jumpCount += 1
                    self.rect.y -= 12
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

    def grab(self, blockGroup):
        if self.lastFace == 'left':
            self.grabCollider = pygame.Rect(self.rect.x - 20, self.rect.y, 20, self.rect.height)
            for block  in blockGroup:
                if self.grabCollider.colliderect(block):
                    self.grabbed.append(block)
                    block.rect.y -= self.rect.height
                    block.rect.x = self.rect.x - self.rect.width
                    return
        else:
            self.grabCollider = pygame.Rect(self.rect.right + 20, self.rect.y, 20, self.rect.height)
            for block in blockGroup:
                if self.grabCollider.colliderect(block):
                    self.grabbed.append(block)
                    block.rect.y -= self.rect.height
                    block.rect.x = self.rect.x - self.rect.width
                    return