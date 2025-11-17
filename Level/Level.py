import pygame
import os
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door

RESOURCES_FILEPATH = os.path.join('Resources', '')

class Level:
    def __init__(self, background, ground, level_id, screen):
        self.background = background      # Background image for the level
        self.ground = ground              # Ground sprite for collision detection
        self.level_id = level_id          # Level identifier

        #all game objects that arent platforms go here
        self.spriteList = pygame.sprite.Group()
        #all block objects go here
        self.blockList = pygame.sprite.Group()
        #all platforms and blovks go here
        self.col_list = pygame.sprite.Group()
        self.col_list.add(ground)
        #all game objects also go here
        self.all_gameObjects = pygame.sprite.Group()
        self.cur_screen = screen
        self.canRobot = Player(0, 0, 16, 26, 1)
        self.endDoor = Door(0, 0, 35, 36, 2)
        self.spriteList.add(self.endDoor)
        self.all_gameObjects.add(self.endDoor)
        self.all_gameObjects.add(self.canRobot)
        self.gameOver = False
        self.eBufferCounter = 0
        self.clock = pygame.time.Clock()


    # Resolve object ID to target object
    def resolveObjIDtoTargetObj(self, id):
        for key, value in self.all_gameObjects:
            if key == id:
                return value
        return None
    
    # Getters and setters
    def getLevelID(self):
        return self.level_id
    
    def getObjects(self):
        return self.object_dict

    def runLevel(self):
        pygame.mixer.music.load(f'{RESOURCES_FILEPATH}Tea K Pea - mewmew.mp3')
        pygame.mixer.music.play(loops=-1)


        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.cur_screen.blit(self.background, (0, 0))
            self.cur_screen.blit(self.ground.image, self.ground.rect)
            if self.eBufferCounter <= 5:
                self.eBufferCounter += 1

            # update each moveable sprite
            for sprite in self.spriteList:
                sprite.update(self.col_list)
                self.cur_screen.blit(sprite.image, sprite.rect)

            # player input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.canRobot.update('left', self.col_list)
                if keys[pygame.K_UP]:
                    self.canRobot.update('up', self.col_list)
            elif keys[pygame.K_RIGHT]:
                self.canRobot.update('right', self.col_list)
                if keys[pygame.K_UP]:
                    self.canRobot.update('up', self.col_list)
            elif keys[pygame.K_UP]:
                self.canRobot.update('up', self.col_list)
            elif keys[pygame.K_e] and self.eBufferCounter > 3:
                if len(self.canRobot.grabbed) == 0:
                    self.canRobot.grab(self.blockList, self.col_list)
                    self.eBufferCounter = 0
                else:
                    self.canRobot.place(self.col_list)
                    self.eBufferCounter = 0

            elif keys[pygame.K_SPACE] and self.endDoor.isOpen():
                if self.canRobot.rect.colliderect(self.endDoor.rect):
                    pygame.display.set_caption("win")
                    self.levelBeaten += 1
                    self.gameOver = True
                    pass

            else:
                self.canRobot.update('stand_right', self.col_list)
            self.cur_screen.blit(self.canRobot.image, self.canRobot.rect)

            pygame.display.flip()
            self.clock.tick(20)



