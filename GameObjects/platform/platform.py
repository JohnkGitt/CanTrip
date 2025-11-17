import pygame


from GameObjects.GameObjects import gameObject
from GameObjects.GameObjects import RESOURCES_FILEPATH

class platform(gameObject):
    def __init__(self, x, y, width, height, id):
        super().__init__(x, y, width, height, id)
        self.image = pygame.image.load(f'{RESOURCES_FILEPATH}platform.png')
