import pygame
from Level.Level import Level
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.Assoc_Block.Assoc_Block import Assoc_Block
from GameObjects.Att_Block.Att_Block import Att_Block


class Level_1(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen)

        self.canRobot.setPOS(500, 500)
        self.endDoor.setPOS(0, 664)


        self.doorBlock = Obj_Block(100, 620, 80, 80, 2, "Door", 2)
        self.col_list.add(self.doorBlock)
        self.spriteList.add(self.doorBlock)
        self.blockList.add(self.doorBlock)
        self.all_gameObjects.add(self.doorBlock)

        # Assoc Block
        self.assocBlock = Assoc_Block(550, 620, 80, 80, 3, "is", self.all_gameObjects)
        self.col_list.add(self.assocBlock)
        self.spriteList.add(self.assocBlock)
        self.blockList.add(self.assocBlock)
        self.all_gameObjects.add(self.assocBlock)

        self.openBlock = Att_Block(1000, 620, 80, 80, 2, "Open", 0)
        self.col_list.add(self.openBlock)
        self.spriteList.add(self.openBlock)
        self.blockList.add(self.openBlock)
        self.all_gameObjects.add(self.openBlock)