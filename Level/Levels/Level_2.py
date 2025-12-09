import pygame
import os
from Level.Level import Level
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.Assoc_Block.Assoc_Block import Assoc_Block
from GameObjects.Att_Block.Att_Block import Att_Block
from GameObjects.platform.platform import platform

RESOURCES_FILEPATH = os.path.join('Resources', '')


class Level_2(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen)

        self.canRobot.setPOS(500, 600)
        self.endDoor.setPOS(10, 640)

        self.plat4 = platform(900, 350, 80, 40, 10)
        self.col_list.add(self.plat4)
        self.spriteList.add(self.plat4)
        self.plat5 = platform(820, 350, 80, 40, 10)
        self.col_list.add(self.plat5)
        self.spriteList.add(self.plat5)


        self.doorBlock = Obj_Block(100, 620, 50, 50, 3, "Door", 2)
        self.col_list.add(self.doorBlock)
        self.spriteList.add(self.doorBlock)
        self.blockList.add(self.doorBlock)
        self.all_gameObjects.add(self.doorBlock)


        self.openBlock = Att_Block(900, 250, 50, 50, 5, "Open", 0)
        self.col_list.add(self.openBlock)
        self.spriteList.add(self.openBlock)
        self.blockList.add(self.openBlock)
        self.all_gameObjects.add(self.openBlock)

        # Assoc Block
        self.assocBlock = Assoc_Block(550, 620, 50, 50, 4, "is", self.all_gameObjects)
        self.col_list.add(self.assocBlock)
        self.spriteList.add(self.assocBlock)
        self.blockList.add(self.assocBlock)
        self.all_gameObjects.add(self.assocBlock)

