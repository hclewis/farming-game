import pygame
import button
from crop import Crop

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# loading images
background = pygame.image.load('./images/background.png')
start = pygame.image.load("./images/buttons/start-button.png").convert_alpha()
harvest = pygame.image.load("./images/buttons/harvest-button.png").convert_alpha()
empty_field = pygame.image.load("./images/empty-field.png").convert_alpha()
seedy_field = pygame.image.load("./images/seedy-field.png").convert_alpha()
carrot_field_1 = pygame.image.load("./images/carrot/carrot-field-1.png").convert_alpha()
carrot_field_2 = pygame.image.load("./images/carrot/carrot-field-2.png").convert_alpha()
carrot_field_3 = pygame.image.load("./images/carrot/carrot-field-3.png").convert_alpha()
carrot_button_image = pygame.image.load("./images/carrot/carrot-button.png").convert_alpha()

# scale images
background_scaled = pygame.transform.scale(background, (1200, 900))
start_small = pygame.transform.scale(start, (200, 100))
harvest_small = pygame.transform.scale(harvest, (300, 90))
empty_field_scaled = pygame.transform.scale(empty_field, (300, 300))

# create crop instances
carrot = Crop("carrot", seedy_field, carrot_field_1, carrot_field_2, carrot_field_3, carrot_button_image)

# create button instances
start_game_button = button.Button(500, 200, start_small, 1)
harvest_button = button.Button(75, 285, harvest_small, 1)
carrot_button = button.Button(75, 720, carrot.button, 1)

# seedling lists
carrot_seedling_list = [carrot.seedy_field, carrot.field_1, carrot.field_2, carrot.field_3]

# timers
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 1000) # every 1000 milliseconds = every 1 second

# game variables
page_state = "menu"
run = True
game_timer = 0
growth_timer = 0
active_growth = False
crops_harvested = True
score = 0

while run:
    screen.blit(background_scaled, (0, 0))
    
    if(page_state == "menu"):
        if start_game_button.draw(screen):
            page_state = "fields"

    if(page_state == "fields"):
        background_scaled.blit(empty_field_scaled, (75, 400))

        if carrot_button.draw(screen):
            if crops_harvested == True:
                crops_harvested = False
                growth_timer = 0
                active_growth = True

        if harvest_button.draw(screen):
            if growth_timer == 4:
                crops_harvested = True
                active_growth = False
                growth_timer = 0
                score += 1
                print(f"{score}")

        if not crops_harvested:
            if active_growth and growth_timer < 4:
                background_scaled.blit(carrot_seedling_list[growth_timer], (75, 400))
            else:
                active_growth = False
                background_scaled.blit(carrot_seedling_list[3], (75, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == TIMEREVENT and page_state == "fields" and active_growth:
            game_timer += 1
            growth_timer += 1

    pygame.display.update()

pygame.quit()