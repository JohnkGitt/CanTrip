import pygame
from GameObjects.GameObjects import gameObject

associationDictionary = {
    "Door": "Open"      # UPDATE THIS DICTIONARY WITH ALL ASSOCIATIONS
}

class Assoc_Block(gameObject):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text
        self.pos1Collider = gameObject.__init__(self.x - self.width, self.y, self.width, self.height)
        self.pos2Collider = gameObject.__init__(self.x, self.y - self.height, self.width, self.height)
        self.pos3Collider = gameObject.__init__(self.x + self.width, self.y, self.width, self.height)
        self.pos4Collider = gameObject.__init__(self.x, self.y + self.height, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def update(self):

        pass

    def get_text(self):
        return self.text
    
    def set_text(self, new_text):
        self.text = new_text

    def prox_Check(self, objBlock, attBlock):
        # Object block must be in pos1 and Attribute block must be in pos3 to be considered a valid association placement.
        if self.pos1Collider.rect.colliderect(objBlock.rect) and self.pos3Collider.rect.colliderect(attBlock.rect):
            return 1
        # Object block must be in pos2 and Attribute block must be in pos4 to be considered a valid association placement.
        if self.pos2Collider.rect.colliderect(objBlock.rect) and self.pos4Collider.rect.colliderect(attBlock.rect):
            return 1
        
        # If Object and Attribute blocks are not in valid positions, return 0.
        return 0
    
    def assoc_Handler(self, objBlock, attBlock):
        validAssociation = False
        
        for key, value in associationDictionary.items():
            if objBlock.get_text() == key and attBlock.get_text() == value:
                validAssociation = True

        if not validAssociation:
            return 0
        


            
