import pygame
from Level.Level import Level
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.platform.platform import platform
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.Assoc_Block.Assoc_Block import Assoc_Block
from GameObjects.Att_Block.Att_Block import Att_Block

class Level_4(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen)

        self.canRobot.setPOS(1100, 600)
        self.endDoor.setPOS(570, 360)
        self.endDoor.open_door()

        self.canRobot.noJumping()

        self.platformList = []
        for i in range(7):
            new_platform = platform(560, 660 - (40 * i), 80, 40, 10)
            self.col_list.add(new_platform)
            self.spriteList.add(new_platform)
            self.platformList.append(new_platform)

        self.jumpBlock = Att_Block(500, 630, 50, 50, 3, "Jump", 0)
        self.col_list.add(self.jumpBlock)
        self.spriteList.add(self.jumpBlock)
        self.blockList.add(self.jumpBlock)
        self.all_gameObjects.add(self.jumpBlock)

        self.botBlock = Obj_Block(1200, 630, 50, 50, 4, "CANRobot", 1)
        self.col_list.add(self.botBlock)
        self.spriteList.add(self.botBlock)
        self.blockList.add(self.botBlock)
        self.all_gameObjects.add(self.botBlock)

        self.assocBlock = Assoc_Block(300, 630, 50, 50, 5, "can", self.all_gameObjects)
        self.col_list.add(self.assocBlock)
        self.spriteList.add(self.assocBlock)
        self.blockList.add(self.assocBlock)
        self.all_gameObjects.add(self.assocBlock)