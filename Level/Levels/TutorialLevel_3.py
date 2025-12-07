import pygame
from Level.Level import Level
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.platform.platform import platform

class TutorialLevel_3(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen)

        self.canRobot.setPOS(1100, 600)
        self.endDoor.setPOS(110, 640)
        self.endDoor.open_door()  # Door starts open in tutorial

        self.level_instructions = [
            "Looks like this wall is blocking your path to get to the exit!",
            "Thankfully, CANRobot has a way around this -- by heading to the right!",
            "Walk to the right, and you'll eventually end up at the door!"
        ]

        self.platformList = []
        for i in range(10):
            new_platform = platform(560, 660 - (40 * i), 80, 40, 10)
            self.col_list.add(new_platform)
            self.spriteList.add(new_platform)
            self.platformList.append(new_platform)