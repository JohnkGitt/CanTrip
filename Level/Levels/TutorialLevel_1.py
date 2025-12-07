import pygame
from Level.Level import Level
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door

class TutorialLevel_1(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen)

        self.canRobot.setPOS(500, 600)
        self.endDoor.setPOS(10, 640)
        self.endDoor.open_door()  # Door starts open in tutorial

        self.level_instructions = [
            "CANRobot wants to escape the facility;",
            "help him by reaching the next level!",
            "Use the [ARROW KEYS] to move to the door and press [SPACE] to proceed."
        ]