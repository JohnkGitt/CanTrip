import pygame
import os
from GameObjects.GameObjects import gameObject
from GameObjects.GameObjects import RESOURCES_FILEPATH
from enum import Enum

class DoorAttributes(Enum):
    OPEN_CLOSED = 0

class Door(gameObject):
    def __init__(self, x, y,  width, height, id):

        super().__init__(x, y, width, height, id)
        self.frame = 0
        self.ID = id
        self.is_open = False

        self.sheet = pygame.image.load(f'{RESOURCES_FILEPATH}door.png')

        self.sheet.set_clip(pygame.Rect(1, 0, 35, 36))

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        self.closed =(1, 0, 35, 36)

        self.opened = (155, 0, 35, 36)

        self.rect.topleft = (x, y)

    def open_door(self):
        self.is_open = True

    def close_door(self):
        self.is_open = False

    def isOpen(self):
        return self.is_open

    def clip(self, clipped_rect):
            if type(clipped_rect) is dict:
                self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
            else:
                self.sheet.set_clip(pygame.Rect(clipped_rect))
            return clipped_rect

    def update(self, collideList):
        if (self.isOpen()):
            self.clip(self.opened)
        else:
            self.clip(self.closed)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def get_frame(self, frame_set):
            self.frame += 1
            if self.frame > (len(frame_set) - 1):
                self.frame = 0

            return frame_set[self.frame]

    def att_Handler(self, attribute):
        if attribute == DoorAttributes.OPEN_CLOSED:
            self.is_open = not self.is_open

    def setPOS(self, X, Y):
        self.rect.x = X
        self.rect.y = Y