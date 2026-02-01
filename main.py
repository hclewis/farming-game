import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# loading images
background = pygame.image.load('./images/background.png')

# scaled images
background_scaled = pygame.transform.scale(background, (1200,900))

run = True

while run == True:
    screen.blit(background_scaled, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()