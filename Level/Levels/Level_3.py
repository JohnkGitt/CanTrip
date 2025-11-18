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

class Level_3(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen)

        self.canRobot.noJumping()
        self.canRobot.setPOS(1000, 600)
        self.endDoor.open_door()

        self.plat1 = platform(10, 600, 80, 40, 10)
        self.col_list.add(self.plat1)
        self.spriteList.add(self.plat1)

        self.plat2 = platform(120, 450, 80, 40, 10)
        self.col_list.add(self.plat2)
        self.spriteList.add(self.plat2)
        self.plat3 = platform(200, 450, 80, 40, 10)
        self.col_list.add(self.plat3)
        self.spriteList.add(self.plat3)

        self.endDoor.setPOS(176, 390)

        self.jumpBlock = Att_Block(1200, 630, 50, 50, 3, "Jump", 0)
        self.col_list.add(self.jumpBlock)
        self.spriteList.add(self.jumpBlock)
        self.blockList.add(self.jumpBlock)
        self.all_gameObjects.add(self.jumpBlock)

        self.botBlock = Obj_Block(300, 630, 50, 50, 4, "CANRobot", 1)
        self.col_list.add(self.botBlock)
        self.spriteList.add(self.botBlock)
        self.blockList.add(self.botBlock)
        self.all_gameObjects.add(self.botBlock)


        self.assocBlock = Assoc_Block(550, 630, 50, 50, 5, "can", self.all_gameObjects)
        self.col_list.add(self.assocBlock)
        self.spriteList.add(self.assocBlock)
        self.blockList.add(self.assocBlock)
        self.all_gameObjects.add(self.assocBlock)
