import pygame
from Level.Level import Level
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.Assoc_Block.Assoc_Block import Assoc_Block
from GameObjects.Att_Block.Att_Block import Att_Block


class Level_2(Level):
    def __init__(self, background, ground, level_id, screen):
        super().__init__(background, ground, level_id, screen)

        self.canRobot.setPOS(500, 200)
        self.endDoor.setPOS(0, 664)

        self.plat1 = pygame.sprite.Sprite()
        self.plat1.rect = pygame.Rect(980, 400, 300, 40)
        self.plat1.image = pygame.Surface((300, 40))
        self.plat1.image.fill((255, 0, 0))
        self.col_list.add(self.plat1)
        self.spriteList.add(self.plat1)

        self.plat2 = pygame.sprite.Sprite()
        self.plat2.rect = pygame.Rect(850, 500, 100, 40)
        self.plat2.image = pygame.Surface((100, 40))
        self.plat2.image.fill((255, 0, 0))
        self.col_list.add(self.plat2)
        self.spriteList.add(self.plat2)



        self.doorBlock = Obj_Block(100, 620, 50, 50, 3, "Door", 2)
        self.col_list.add(self.doorBlock)
        self.spriteList.add(self.doorBlock)
        self.blockList.add(self.doorBlock)
        self.all_gameObjects.add(self.doorBlock)


        self.openBlock = Att_Block(1200, 300, 50, 50, 5, "Open", 0)
        self.col_list.add(self.openBlock)
        self.spriteList.add(self.openBlock)
        self.blockList.add(self.openBlock)
        self.all_gameObjects.add(self.openBlock)

        self.door2Block = Obj_Block(100, 540, 50, 50, 6, "Door", 2)
        self.col_list.add(self.door2Block)
        self.spriteList.add(self.door2Block)
        self.blockList.add(self.door2Block)
        self.all_gameObjects.add(self.door2Block)

        # Assoc Block
        self.assocBlock = Assoc_Block(550, 620, 50, 50, 4, "is", self.all_gameObjects)
        self.col_list.add(self.assocBlock)
        self.spriteList.add(self.assocBlock)
        self.blockList.add(self.assocBlock)
        self.all_gameObjects.add(self.assocBlock)

