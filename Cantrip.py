import pygame
from GameObjects.player.Player import Player

pygame.init()
screen_w = 1280
screen_h = 720

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("CanTrip")
clock = pygame.time.Clock()

ground = pygame.sprite.Sprite()
ground.rect = pygame.Rect(0, 700, screen_w, 20)
col_list = pygame.sprite.Group()
col_list.add(ground)

canRobot = Player((0,0), col_list)
canRobot.setPOS((screen_w // 2), (screen_h // 2))
all_gameObjects = pygame.sprite.Group()

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
    canRobot.handle_event(event, col_list)
    screen.fill((0,0,0))
    screen.blit(canRobot.image, canRobot.rect)

    pygame.display.flip()

    clock.tick(20)

pygame.quit()

