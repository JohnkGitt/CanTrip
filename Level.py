import pygame
from Grid import Grid

LEVEL_WIDTH = Grid.GRID_WIDTH
LEVEL_HEIGHT = Grid.GRID_LENGTH

class Level:
    def __init__(self, background, ground, object_dict, level_id):
        self.background = background      # Background image for the level
        self.ground = ground              # Ground sprite for collision detection
        self.object_dict = object_dict    # Dictionary of game objects in the level
        self.level_id = level_id          # Level identifier
        levelBeaten = 0

    # Resolve object ID to target object
    def resolveObjIDtoTargetObj(self, id):
        for key, value in self.object_dict.items():
            if key == id:
                return value
        return None
    
    # Getters and setters
    def getLevelID(self):
        return self.level_id
    
    def getObjects(self):
        return self.object_dict
    
    def isLevelBeaten(self):
        return self.levelBeaten
    
    def setLeveLBeaten(self, levelBeaten):
        self.levelBeaten = levelBeaten