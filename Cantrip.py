import pygame
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.Obj_Block.Obj_Block import Obj_Block
from GameObjects.Att_Block.Att_Block import Att_Block

pygame.init()
screen_w = 1280
screen_h = 720

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("CanTrip")
clock = pygame.time.Clock()

ground = pygame.sprite.Sprite()
ground.rect = pygame.Rect(0, 700, screen_w, 20)

spriteList = pygame.sprite.Group()
col_list = pygame.sprite.Group()
col_list.add(ground)

#door
endDoor = Door(0, 700, 35, 36, 1)
endDoor.setPOS(0,664)
spriteList.add(endDoor)

#player
canRobot = Player((0,0), col_list)
canRobot.setPOS((screen_w // 2), (screen_h // 2))
all_gameObjects = pygame.sprite.Group()

#object Block
doorBlock = Obj_Block(100, 620, 80, 80, 2, 'door', 1)
col_list.add(doorBlock)
spriteList.add(doorBlock)

#attribute Block
openBlock = Att_Block(1000, 620, 80, 80, 2, 'door', 1)
col_list.add(openBlock)
spriteList.add(openBlock)


def resolveObjIDtoTargetObj(id):
    for obj in all_gameObjects:
        if obj.getID() == id:
            return obj
    return None

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill((0,0,0))

    #update each moveable sprite
    for sprite in spriteList:
        sprite.update(col_list)
        screen.blit(sprite.image, sprite.rect)


    #player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        canRobot.update('left', col_list)
        if keys[pygame.K_UP]:
            canRobot.update('up', col_list)
    elif keys[pygame.K_RIGHT]:
        canRobot.update('right', col_list)
        if keys[pygame.K_UP]:
            canRobot.update('up', col_list)
    elif keys[pygame.K_UP]:
        canRobot.update('up', col_list)
    elif keys[pygame.K_SPACE] and endDoor.isOpen():
        if canRobot.rect.colliderect(canRobot.rect):
            pygame.display.set_caption("win")
            pass

    else:
        canRobot.update('stand_right', col_list)
    screen.blit(canRobot.image, canRobot.rect)

    pygame.display.flip()

    clock.tick(20)

pygame.quit()

