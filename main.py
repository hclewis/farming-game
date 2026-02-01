import pygame
import button

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# loading images
background = pygame.image.load('./images/background.png')
start = pygame.image.load("./images/buttons/start-button.png").convert_alpha()
empty_field = pygame.image.load("./images/empty-field.png").convert_alpha()

# scale images
background_scaled = pygame.transform.scale(background, (1200, 900))
start_small = pygame.transform.scale(start, (200, 100))
empty_field_scaled = pygame.transform.scale(empty_field, (300, 300))

# create button instances
start_game_button = button.Button(500, 200, start_small, 1)

# timers
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 1000) # every 1000 milliseconds = every 1 second

# game variables
page_state = "menu"
run = True
game_timer = 0

while run:
    screen.blit(background_scaled, (0, 0))
    
    if(page_state == "menu"):
        if start_game_button.draw(screen):
            page_state = "fields"

    if(page_state == "fields"):
        background_scaled.blit(empty_field_scaled, (75, 400))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == TIMEREVENT:
            game_timer += 1
            print(f"{game_timer}")

    pygame.display.update()

pygame.quit()