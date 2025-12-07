import pygame
import os
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.Assoc_Block.Assoc_Block import Assoc_Block
from GameObjects.Att_Block.Att_Block import Att_Block
from Level.Levels.TutorialLevel_1 import TutorialLevel_1
from Level.Levels.TutorialLevel_2 import TutorialLevel_2
from Level.Levels.Level_1 import Level_1
from Level.Levels.Level_2 import Level_2
from Level.Levels.Level_3 import Level_3
from Menu import Menu

# Intialize Pygame
pygame.init()
pygame.mixer.init()

# Define screen dimensions
screen_w = 1280
screen_h = 720
screen = pygame.display.set_mode((screen_w, screen_h))

# Load menu assets and create menu
bg = pygame.image.load(os.path.join('Resources', 'background 2.jpg'))
controls_text = "Controls:\n- Use the [ARROW KEYS] to move and jump\n- Press [E] to grab and place blocks\n- Arrange blocks to form statements (e.g. \"Door is Open\")\n- Reach the door and hit [SPACE] to proceed to the next level!\n- Escape the factory to win!"
menu = Menu(screen, ["Start", "How To Play", "Quit"], "CANTrip", bg=bg, font='arial')
controls_menu = Menu(screen, ["Back"], "How To Play", controls_text, bg=bg, font='arial', additional_text_size=24)
inMenu = True

# Main menu loop
while (inMenu):
    choice = menu.run()
    # If choice is "Quit"
    if choice is None or choice == 2:
        pygame.quit()
        exit()
    # If choice is "How To Play"
    elif choice == 1:
        back_choice = controls_menu.run()
        if back_choice is None:
            pygame.quit()
            exit()
    # If choice is "Start"
    else:
        inMenu = False

cwd= os.getcwd()
pygame.display.set_caption("CanTrip")
clock = pygame.time.Clock()

ground = pygame.sprite.Sprite()
ground.rect = pygame.Rect(0, 700, screen_w, 20)
ground.image = pygame.image.load(os.path.join('Resources', 'floor.png'))

firstTutorialLV = TutorialLevel_1(bg, ground, 0, screen)
firstTutorialLV.runLevel()

secondTutorialLV = TutorialLevel_2(bg, ground, 1, screen)
secondTutorialLV.runLevel()

firstLV = Level_1(bg, ground, 2, screen)
firstLV.runLevel()

secondLV = Level_2(bg, ground, 3, screen)
secondLV.runLevel()

thirdLV = Level_3(bg, ground, 4, screen)
thirdLV.runLevel()

pygame.quit()


