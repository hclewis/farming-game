import pygame
import button

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# loading images
background = pygame.image.load('./images/background.png')
start = pygame.image.load("./images/buttons/start-button.png").convert_alpha()

#scale images
background_scaled = pygame.transform.scale(background, (1200, 900))
start_small = pygame.transform.scale(start, (200, 100))

#create button instances
start_game_button = button.Button(500, 200, start_small, 1)

run = True

while run:
    screen.blit(background_scaled, (0, 0))
    
    start_game_button.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()