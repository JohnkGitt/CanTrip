import pygame

class gameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, id):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)  # Default color black
        self.image = pygame.Surface((self.width, self.height)) # PLACEHOLDER
        self.rect = self.image.get_rect()
        self.id = id
    
    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def setPOS(self, x, y):
        self.x = x
        self.y = y

    def getPOS(self):
        return (self.x, self.y)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

