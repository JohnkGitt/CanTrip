import pygame
from GameObjects.GameObjects import gameObject


class Player(gameObject):
    def __init__(self, position, collideList):
        self.ID = 1
        self.CList = collideList

        self.sheet = pygame.image.load('PSprites.png')

        #16x26
        self.sheet.set_clip(pygame.Rect(0, 0, 16, 26))

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        self.rect.topleft = position

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
            if direction == 'left':
                self.clip(self.leftWalkStates)
                self.rect.x -= 5
            if direction == 'right':
                self.clip(self.rightWalkStates)
                self.rect.x += 5
            if direction == 'stand_left':
                self.clip(self.leftIdleStates)
            if direction == 'stand_right':
                self.clip(self.rightIdleStates)
            if not self.onGround(collideList):
                self.rect.y += 5
            if self.isJumping:
                if self.jumpCount == 20:
                    self.jumpCount = 0
                    self.isJumping = False
                if self.jumpCount > 14:
                    self.jumpCount += 1
                    self.rect.y -= 5
                else:
                    self.jumpCount += 1
                    self.rect.y -= 10
            self.image = self.sheet.subsurface(self.sheet.get_clip())

    def onGround(self, collideList):
        for sprite in collideList:
            if self.rect.colliderect(sprite.rect):
                return True
        return False

    def handle_event(self, event, collision):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left', collision)
            if event.key == pygame.K_RIGHT:
                self.update('right', collision)
            if event.key == pygame.K_UP and self.onGround(collision):
                self.isJumping = True
                self.update('stand_right', collision)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.update('stand_left', collision)
            if event.key == pygame.K_RIGHT:
                self.update('stand_right', collision)



    def getID(self):
        return self.ID

    def setPOS(self, X, Y):
        self.rect.x = X
        self.rect.y = Y

    def getPOS(self):
        return self.rect.x, self.rect.y

    def att_Handler(self):
        pass