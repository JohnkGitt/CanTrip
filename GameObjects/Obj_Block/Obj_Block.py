import pygame
from GameObjects.GameObjects import gameObject

class Obj_Block(gameObject):
    def __init__(self, x, y, width, height, id, text):
        super().__init__(x, y, width, height, id)
        self.text = text

    def get_text(self):
        return self.text
    
    def set_text(self, text):
        self.text = text
