import pygame
from Level.Level import Level
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.Assoc_Block.Assoc_Block import Assoc_Block
from GameObjects.Att_Block.Att_Block import Att_Block


class FinalLV(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen, cutscene=True)

        self.canRobot.setPOS(10, 640)
        self.endDoor.setPOS(10, 640)
        self.endDoor.open_door()

        self.level_instructions = [
            "You've made it! CANRobot has escaped the factory thanks to your help.",
            "Thank you for playing!"
        ]