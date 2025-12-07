import pygame
from Level.Level import Level
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.platform.platform import platform
from GameObjects.Obj_Block.Obj_Block import Obj_Block

class TutorialLevel_2(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen)

        self.canRobot.setPOS(500, 600)
        self.endDoor.setPOS(10, 440)
        self.endDoor.open_door()  # Door starts open in tutorial

        self.level_instructions = [
            "Looks like you'll need to get up to the platform to exit.",
            "Grab that block with [E] and place it next to you with [E] to get to the platform.",
            "Then, jump to the platform with [UP ARROW] and reach the door to proceed."
        ]

        self.plat1 = platform(0, 500, 80, 40, 10)
        self.col_list.add(self.plat1)
        self.spriteList.add(self.plat1)

        self.botBlock = Obj_Block(300, 630, 50, 50, 4, "CANRobot", 1)
        self.col_list.add(self.botBlock)
        self.spriteList.add(self.botBlock)
        self.blockList.add(self.botBlock)
        self.all_gameObjects.add(self.botBlock)