import os
import pygame


RESOURCES_FILEPATH = os.path.join('Resources', '')

class gameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, id):
        super().__init__()
        self.width = width
        self.height = height
        self.color = (255, 255, 255)  # Default color black
        self.image = pygame.Surface((self.width, self.height)) # PLACEHOLDER
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = id
    
    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def setPOS(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def getPOS(self):
        return (self.rect.x, self.rect.y)
    


