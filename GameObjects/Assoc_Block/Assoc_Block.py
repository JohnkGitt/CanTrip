import pygame
from GameObjects.Door.Door import DoorAttributes
from GameObjects.player.Player import PlayerAttributes
from GameObjects.Obj_Block import Obj_Block
from GameObjects.Att_Block import Att_Block
from GameObjects.GameObjects import gameObject

associationDictionary = {
    ("Door", "Open"): DoorAttributes.OPEN_CLOSED,      # UPDATE THIS DICTIONARY WITH ALL ASSOCIATIONS
    ("CANRobot", "Jump"): PlayerAttributes.JUMP,
    ("CANRobot", "Walk Left"): PlayerAttributes.WALK_LEFT,
    ("CANRobot", "Walk Right"): PlayerAttributes.WALK_RIGHT,
    ("CANRobot", "Grab"): PlayerAttributes.GRAB
}

class Assoc_Block(gameObject):
    def __init__(self, x, y, width, height, id, text):
        super().__init__(x, y, width, height, id)
        self.text = text

        self.sheet = pygame.image.load('assoc_block.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 80, 80))
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.pos1Collider = gameObject(
            x = self.rect.x - (self.width // 3),
            y = self.rect.y,
            width = self.width // 3,
            height = self.height,
            id = 1000
            )
        self.pos2Collider = gameObject(
            x = self.rect.x,
            y = self.rect.y - (self.height // 3),
            width = self.width,
            height = self.height // 3,
            id = 1001
            )
        self.pos3Collider = gameObject(
            x = self.rect.x + (self.width // 3), 
            y = self.rect.y,
            width = self.width // 3,
            height = self.height,
            id = 1002
            )    
        self.pos4Collider = gameObject(
            x = self.rect.x,
            y = self.rect.y + (self.height // 3),
            width = self.width,
            height = self.height // 3,
            id = 1003
            )
        self.associationActive = False
        self.objBlockAssociation = None
        self.attBlockAssociation = None
        self._cantrip = None # Lazy load of Cantrip module to avoid circular import

    def _get_cantrip(self):
        # Lazy import of Cantrip (only called once)
        if self._cantrip is None:
            import Cantrip
            self._cantrip = Cantrip
        return self._cantrip

    def update(self, collideList):
         # Update pos colliders
        self.pos1Collider.setPOS(self.rect.x - self.width, self.rect.y)
        self.pos2Collider.setPOS(self.rect.x, self.rect.y - self.height)
        self.pos3Collider.setPOS(self.rect.x + self.width, self.rect.y)
        self.pos4Collider.setPOS(self.rect.x, self.rect.y + self.height)

        # Reset
        self.objBlockAssociation = None
        self.attBlockAssociation = None

        # Check only Obj_Block and Att_Block
        for obj in collideList:
            if not isinstance(obj, (Obj_Block, Att_Block)):
                continue

            rect = obj.rect

            if self.pos1Collider.rect.colliderect(rect) and isinstance(obj, Obj_Block):
                self.objBlockAssociation = obj
            elif self.pos2Collider.rect.colliderect(rect) and isinstance(obj, Obj_Block):
                self.objBlockAssociation = obj
            elif self.pos3Collider.rect.colliderect(rect) and isinstance(obj, Att_Block):
                self.attBlockAssociation = obj
            elif self.pos4Collider.rect.colliderect(rect) and isinstance(obj, Att_Block):
                self.attBlockAssociation = obj

        # Now handle association
        if self.objBlockAssociation and self.attBlockAssociation:
            if self.prox_Check(self.objBlockAssociation, self.attBlockAssociation):
                if not self.associationActive:
                    self.assoc_Handler(self.objBlockAssociation, self.attBlockAssociation)
                    self.associationActive = True
            else:
                if self.associationActive:
                    self.assoc_Handler(self.objBlockAssociation, self.attBlockAssociation)  # deactivate
                    self.associationActive = False
                    self.objBlockAssociation = None
                    self.attBlockAssociation = None


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
        Cantrip = self._get_cantrip()  # This will need to be changed. The associated objID to object resolution will take place in a separate class in the future
        associationPair = (objBlock.get_text(), attBlock.get_text())
        targetChange = None
        
        # Checks if (obj, att) association is found within defined association dictionary
        for assocPair, targetChange in associationDictionary.items():
            if associationPair == assocPair:
                # If found, resolve pair to a integer that marks a specific change to be made to target object
                # Resolve object ID to target object within Cantrip game world and call its associated att_Handler method with targetChange
                Cantrip.resolveObjIDtoTargetObj(objBlock.getID()).att_Handler(targetChange)
                break
                
        


        


            
