import pygame
from GameObjects.GameObjects import gameObject
from enum import Enum

class DoorAttributes(Enum):
    OPEN_CLOSED = 0

class Door(gameObject):
    def __init__(self, x, y, width, height, id):
        super().__init__(x, y, width, height, id)
        self.is_open = False

    def open_door(self):
        self.is_open = True

    def close_door(self):
        self.is_open = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def att_Handler(self, attribute):
        if attribute == DoorAttributes.OPEN:
            self.is_open = not self.is_open