import pygame
from GameObjects.Door import DoorAttributes
from GameObjects.player import PlayerAttributes
from GameObjects.Obj_Block import Obj_Block
from GameObjects.Att_Block import Att_Block
from GameObjects.GameObjects import gameObject
from Cantrip import Cantrip

associationDictionary = {
    ("Door", "Open"): DoorAttributes.OPEN,      # UPDATE THIS DICTIONARY WITH ALL ASSOCIATIONS
    ("Door", "Close"): DoorAttributes.CLOSED,
    ("CANRobot", "Jump"): PlayerAttributes.JUMP,
    ("CANRobot", "Walk Left"): PlayerAttributes.WALK_LEFT,
    ("CANRobot", "Walk Right"): PlayerAttributes.WALK_RIGHT,
    ("CANRobot", "Grab"): PlayerAttributes.GRAB
}

class Assoc_Block(gameObject):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text
        self.pos1Collider = gameObject.__init__(self.x - self.width, self.y, self.width, self.height)
        self.pos2Collider = gameObject.__init__(self.x, self.y - self.height, self.width, self.height)
        self.pos3Collider = gameObject.__init__(self.x + self.width, self.y, self.width, self.height)
        self.pos4Collider = gameObject.__init__(self.x, self.y + self.height, self.width, self.height)
        self.posColliderList = pygame.sprite.Group()
        self.posColliderList = (self.pos1Collider, self.pos2Collider, self.pos3Collider, self.pos4Collider)
        self.associationActive = False
        self.objBlockAssociation = None
        self.attBlockAssociation = None

    def update(self):
         # Update collider positions relative to Assoc_Block position
        self.pos1Collider.setPOS(self.x - self.width, self.y)
        self.pos2Collider.setPOS(self.x, self.y - self.height)
        self.pos3Collider.setPOS(self.x + self.width, self.y)
        self.pos4Collider.setPOS(self.x, self.y + self.height)

        # Find all gameObjects that collide with any of the position colliders
        for gameObj in Cantrip.all_gameObjects:
            collidingObjects = pygame.sprite.spritecollide(gameObj, self.posColliderList, False)
            # Resolve colliding objects into Obj_Block and Att_Block references (if any)
            for obj in collidingObjects:
                if isinstance(obj, Obj_Block):
                    self.objBlockAssociation = obj
                if isinstance(obj, Att_Block):
                    self.attBlockAssociation = obj
        
        # If objBlock and attBlock were resolved...
        if self.objBlockAssociation and self.attBlockAssociation:
            # Check proximity and check if association is already active
            if self.prox_Check(self.objBlockAssociation, self.attBlockAssociation) and not self.associationActive:
                # If proximity check is valid and association not already active, activate association between attribute and object
                self.assoc_Handler(self.objBlockAssociation, self.attBlockAssociation)
                self.associationActive = True
            if self.associationActive and not self.prox_Check(self.objBlockAssociation, self.attBlockAssociation):
                # If proximity check is invalid and association is active, deactivate association between attribute and object
                self.associationActive = False
                self.assoc_Handler(self.objBlockAssociation, self.attBlockAssociation)
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
        validAssociation = False
        associationPair = (objBlock.get_text(), attBlock.get_text())
        targetChange = None
        
        # Checks if (obj, att) association is found within defined association dictionary
        for key in associationDictionary.items():
            if associationPair == key:
                # If found, resolve pair to a integer that marks a specific change to be made to target object
                targetChange = associationDictionary[key]
                validAssociation = True

        if not validAssociation:
            return 0
        
        # Resolve object ID to target object within Cantrip game world and call its associated att_Handler method with targetChange
        Cantrip.resolveObjIDtoTargetObj(objBlock.getID()).att_Handler(targetChange)
        


        


            
