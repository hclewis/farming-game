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
seedy_field = pygame.image.load("./images/seedy-field.png").convert_alpha()
carrot_field_1 = pygame.image.load("./images/carrot/carrot-field-1.png").convert_alpha()
carrot_field_2 = pygame.image.load("./images/carrot/carrot-field-2.png").convert_alpha()
carrot_field_3 = pygame.image.load("./images/carrot/carrot-field-3.png").convert_alpha()

# scale images
background_scaled = pygame.transform.scale(background, (1200, 900))
start_small = pygame.transform.scale(start, (200, 100))
empty_field_scaled = pygame.transform.scale(empty_field, (300, 300))
seedy_field_scaled = pygame.transform.scale(seedy_field, (300, 300))
carrot_field_1_scaled = pygame.transform.scale(carrot_field_1, (300, 300))
carrot_field_2_scaled = pygame.transform.scale(carrot_field_2, (300, 300))
carrot_field_3_scaled = pygame.transform.scale(carrot_field_3, (300, 300))

# seedling lists
carrot_seedling_list = [seedy_field_scaled, carrot_field_1_scaled, carrot_field_2_scaled, carrot_field_3_scaled]

# create button instances
start_game_button = button.Button(500, 200, start_small, 1)

# timers
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 1000) # every 1000 milliseconds = every 1 second

# game variables
page_state = "menu"
run = True
game_timer = 0
growth_timer = 0

while run:
    screen.blit(background_scaled, (0, 0))
    
    if(page_state == "menu"):
        if start_game_button.draw(screen):
            growth_timer = 0
            page_state = "fields"

    if(page_state == "fields"):
        background_scaled.blit(empty_field_scaled, (75, 400))
        if growth_timer < 4:
            background_scaled.blit(carrot_seedling_list[growth_timer], (75, 400))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == TIMEREVENT:
            game_timer += 1
            growth_timer += 1

    pygame.display.update()

pygame.quit()