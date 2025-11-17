import pygame
import os
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.Assoc_Block.Assoc_Block import Assoc_Block
from GameObjects.Att_Block.Att_Block import Att_Block
from Level.Levels.Level_1 import Level_1
from Level.Levels.Level_2 import Level_2



pygame.init()
pygame.mixer.init()
screen_w = 1280
screen_h = 720
font = pygame.font.SysFont('arial', 32)
status_text = "Press [E] to grab/place blocks | [SPACE] to win when in front of an open door"
more_info = "left and right arrows to move | up arrow to jump | arrange the blocks to make a statement!"
text_surface = font.render(status_text, True, (255, 255, 255))
text_surface2 = font.render(more_info, True, (255, 255, 255))

cwd= os.getcwd()
bg = pygame.image.load(os.path.join('Resources', 'background 2.jpg'))
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("CanTrip")
clock = pygame.time.Clock()

ground = pygame.sprite.Sprite()
ground.rect = pygame.Rect(0, 700, screen_w, 20)
ground.image = pygame.image.load(os.path.join('Resources', 'floor.png'))



firstLV = Level_1(bg, ground, 1, screen)
firstLV.runLevel()
secondLV = Level_2(bg, ground, 1, screen)
secondLV.runLevel()




pygame.quit()


