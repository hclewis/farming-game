import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()