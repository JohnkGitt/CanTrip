import pygame
from GameObjects.Door.Door import DoorAttributes
from GameObjects.player.Player import PlayerAttributes
from GameObjects.Obj_Block import Obj_Block
from GameObjects.Att_Block import Att_Block
from GameObjects.GameObjects import gameObject
from GameObjects.GameObjects import RESOURCES_FILEPATH

associationDictionary = {
    ("Door", "Open"): DoorAttributes.OPEN_CLOSED,      # UPDATE THIS DICTIONARY WITH ALL ASSOCIATIONS
    ("CANRobot", "Jump"): PlayerAttributes.JUMP,
    ("CANRobot", "Walk Left"): PlayerAttributes.WALK_LEFT,
    ("CANRobot", "Walk Right"): PlayerAttributes.WALK_RIGHT,
    ("CANRobot", "Grab"): PlayerAttributes.GRAB
}

class Assoc_Block(gameObject):
    def __init__(self, x, y, width, height, id, text, objList):
        super().__init__(x, y, width, height, id)
        self.text = text        
        self.isGrabbed = False
        self.sheet = pygame.image.load(f'{RESOURCES_FILEPATH}assoc_block.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 80, 80))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.objectList = objList

        # Collider directly to the left of assoc block
        self.pos1Collider = gameObject(
            x = self.rect.x - (self.width // 3),
            y = self.rect.y,
            width = self.width // 3,
            height = self.height,
            id = 1000
            )
        # Collider directly above assoc block
        self.pos2Collider = gameObject(
            x = self.rect.x,
            y = self.rect.y - (self.height // 3),
            width = self.width,
            height = self.height // 3,
            id = 1001
            )
        # Collider directly to the right of assoc block
        self.pos3Collider = gameObject(
            x = self.rect.x + (self.width // 3), 
            y = self.rect.y,
            width = self.width // 3,
            height = self.height,
            id = 1002
            )
        # Collider directly below assoc block
        self.pos4Collider = gameObject(
            x = self.rect.x,
            y = self.rect.y + (self.height // 3),
            width = self.width,
            height = self.height // 3,
            id = 1003
            )
        self.associationActive = False  # Tracks whether an association is active
        self.objBlockAssociation = None # Tracks object block colliding with association block
        self.attBlockAssociation = None # Tracks attribute block colliding with association block
        self.removeAssociation = False  # Tracks whether an association should be removed

    def update(self, collideList):
        # Update collider positions
        self.pos1Collider.setPOS(self.rect.x - self.width, self.rect.y)
        self.pos2Collider.setPOS(self.rect.x, self.rect.y - self.height)
        self.pos3Collider.setPOS(self.rect.x + self.width, self.rect.y)
        self.pos4Collider.setPOS(self.rect.x, self.rect.y + self.height)

        # Default: unset associations, we'll reassign if any block is touching
        prevObjBlock = self.objBlockAssociation
        prevAttBlock = self.attBlockAssociation
        self.objBlockAssociation = None
        self.attBlockAssociation = None

        for obj in collideList:
            isObjBlock = isinstance(obj, Obj_Block.Obj_Block)
            isAttBlock = isinstance(obj, Att_Block.Att_Block)
            rect = obj.rect

            # Assign if a block is currently touching relevant collider
            if (self.pos1Collider.rect.colliderect(rect) or self.pos2Collider.rect.colliderect(rect)) and isObjBlock:
                self.objBlockAssociation = obj
            if (self.pos3Collider.rect.colliderect(rect) or self.pos4Collider.rect.colliderect(rect)) and isAttBlock:
                self.attBlockAssociation = obj

        # Now handle association/deassociation
        if self.objBlockAssociation and self.attBlockAssociation:
            if self.prox_Check(self.objBlockAssociation, self.attBlockAssociation):
                if not self.associationActive:
                    self.assoc_Handler(self.objBlockAssociation, self.attBlockAssociation)
                    self.associationActive = True
        else:
            # If any block moved away, association is broken
            if self.associationActive:
                self.assoc_Handler(prevObjBlock, prevAttBlock)
                self.associationActive = False

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
        associationPair = (objBlock.get_text(), attBlock.get_text())
        targetChange = None
        
        # Checks if (obj, att) association is found within defined association dictionary
        for assocPair, targetChange in associationDictionary.items():
            if associationPair == assocPair:
                # If found, resolve pair to a integer that marks a specific change to be made to target object
                # Resolve object ID to target object within Cantrip game world and call its associated att_Handler method with targetChange
                self.resolveObjIDtoTargetObj(objBlock.getID()).att_Handler(targetChange)
                break

    def update2(self, X, Y):
        self.rect.x -= X
        self.rect.y -= Y

    def changeGrabbed(self):
        self.isGrabbed = not self.isGrabbed

    def collide_adjust(self, colliders):
        for sprite in colliders:
            if self.rect.colliderect(sprite.rect):
                ydiff = self.rect.bottom - sprite.rect.top
                ldiff = sprite.rect.right - self.rect.left
                rdiff = self.rect.right - sprite.rect.left
                if ydiff < ldiff and ydiff < rdiff:
                    self.rect.y -= ydiff
                elif ldiff > rdiff:
                    self.rect.x += ldiff
                else:
                    self.rect.x += rdiff

    def resolveObjIDtoTargetObj(self, id):
        for obj in self.objectList:
            if obj.getID() == id:
                return obj
        return None

                
        


        


            
