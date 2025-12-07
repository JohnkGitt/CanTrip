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
    def __init__(self, x, y, width, height, id, has_physics=True, grabbable=False):
        self.has_physics = has_physics
        self.grabbable = grabbable
        super().__init__(x, y, width, height, id, has_physics=has_physics, grabbable=grabbable)
        self.ID = id
        self.lastFace = ''
        self.sheet = pygame.image.load(f'{RESOURCES_FILEPATH}PSprites_scaled2x.png')
        self.width = width
        self.height = height
        self.finalx = 0
        self.finaly = 0

        self.canJump = True

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
        self.guide = pygame.sprite.Sprite()
        self.guide.rect = pygame.Rect(100, 0, 55, 10)
        self.guide.image = pygame.image.load(f'{RESOURCES_FILEPATH}guide.png')
        self.guide.image.set_alpha(0)
        self.isGuideLeft = False


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

            self.rect.y += self.bottom_collide(collideList)
            if self.isJumping:
                roof = self.top_collide(collideList)
                if self.jumpCount == 20:
                    self.jumpCount = 0
                    self.isJumping = False
                if self.jumpCount > 14:
                    if roof < 12:
                        self.rect.y -= roof
                    else:
                        self.rect.y -= 17
                    self.jumpCount += 1
                else:
                    if roof < 15:
                        self.rect.y -= roof
                    else:
                        self.rect.y -= 20
                    self.jumpCount += 1

            screen_width = None
            surface = pygame.display.get_surface()
            if surface:
                screen_width = surface.get_width()

            if direction == 'left':
                self.clip(self.leftWalkStates)
                step = self.left_collide(collideList)
                attempted_x = self.rect.x - step

                if screen_width is None or attempted_x >= 0:
                    # normal move (no wrap)
                    self.rect.x = attempted_x
                else:
                    # would go off left edge -> attempt wrap to right side
                    wrap_x = attempted_x + screen_width
                    temp = self.rect.copy()
                    temp.x = wrap_x
                    if not self._has_collision_at(temp, collideList):
                        self.rect.x = wrap_x
                    else:
                        # blocked by a collision on the wrapped side -> don't move
                        pass
                self.lastFace = 'left'
                self.setGuideLeft()

            if direction == 'right':
                self.clip(self.rightWalkStates)
                step = self.right_collide(collideList)
                attempted_x = self.rect.x + step

                if screen_width is None or (attempted_x + self.rect.width) <= screen_width:
                    # normal move
                    self.rect.x = attempted_x
                else:
                    # would go off right edge -> attempt wrap to left side
                    wrap_x = attempted_x - screen_width
                    temp = self.rect.copy()
                    temp.x = wrap_x
                    if not self._has_collision_at(temp, collideList):
                        self.rect.x = wrap_x
                    else:
                        # blocked by a collision on the wrapped side -> don't move
                        pass
                self.lastFace = 'right'
                self.setGuideRight()
            
            if direction == 'stand_left':
                self.clip(self.leftIdleStates)
            if direction == 'stand_right':
                self.clip(self.rightIdleStates)
            if direction == 'up' and self.canJump:
                self.jump(collideList)
            finalx = finalx - self.rect.x
            finaly = finaly - self.rect.y

            if len(self.grabbed) > 0:
                self.grabbed[0].update2(finalx, finaly)

            self.image = self.sheet.subsurface(self.sheet.get_clip())

    def _has_collision_at(self, test_rect, collideList):
        count = 0
        for sprite in collideList:
            if count > 0:
                if test_rect.colliderect(sprite.rect):
                    return True
            count += 1
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

    def top_collide(self, collideList):
        count = 0
        smallest = 21
        for sprite in collideList:
            if count > 0:
                dif = self.rect.top - sprite.rect.bottom
                cond1 = smallest > dif >= 0
                cond2 = self.rect.left < sprite.rect.right and sprite.rect.left < self.rect.right
                if cond1 and cond2:
                    smallest = dif
            count += 1
        return smallest

    def bottom_collide(self, collideList):
        smallest = 10
        for sprite in collideList:
                dif =  sprite.rect.top - self.rect.bottom
                cond1 = smallest > dif >= 0
                cond2 = self.rect.left < sprite.rect.right and sprite.rect.left < self.rect.right
                if cond1 and cond2:
                    smallest = dif
        return smallest

    def jump(self, collideList):
        if not(self.isJumping) and self.bottom_collide(collideList)  == 0:
            self.isJumping = True
            self.jumpSound.play()
        if self.isJumping and self.jumpCount < 6:
            self.rect.y -= 20


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
                    self.guide.image.set_alpha(255)
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
                    self.guide.image.set_alpha(255)
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
        self.guide.image.set_alpha(0)
        self.placeSound.play()

    def getID(self):
        return self.ID

    def att_Handler(self, target):
        if target == PlayerAttributes.JUMP:
            self.canJump = not self.canJump

    def noJumping(self):
        self.canJump = False

    def changeGuideDir(self):
        self.isGuideLeft = not self.isGuideLeft
        self.guide.image = pygame.transform.flip(self.guide.image, True, False)

    def setGuideLeft(self):
        self.guide.rect.right = self.rect.left
        self.guide.rect.y = self.rect.y + 42
        if not self.isGuideLeft:
            self.changeGuideDir()

    def setGuideRight(self):
        self.guide.rect.left = self.rect.right
        self.guide.rect.y = self.rect.y + 42
        if self.isGuideLeft:
            self.changeGuideDir()