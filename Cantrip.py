import pygame
from GameObjects.player.Player import Player

pygame.init()
screen_w = 1280
screen_h = 720

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("CanTrip")
clock = pygame.time.Clock()

canRobot = Player((0,0))
canRobot.setPOS((screen_w // 2), (screen_h // 2))

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    canRobot.handle_event(event)
    screen.fill((0,0,0))
    screen.blit(canRobot.image, canRobot.rect)

    pygame.display.flip()

    clock.tick(20)

pygame.quit()

