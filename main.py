import pygame
import button
from crop import Crop
from field import Field

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# colours
text_colour_1 = (255,255,255)

# fonts
font_1 = pygame.font.SysFont("arialblack", 40)

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
carrot_icon_image = pygame.image.load("./images/carrot/carrot-icon.png").convert_alpha()

# scale images
background_scaled = pygame.transform.scale(background, (1200, 900))
start_small = pygame.transform.scale(start, (200, 100))
harvest_small = pygame.transform.scale(harvest, (300, 90))

# create field instances
field_1 = Field(empty_field)
field_2 = Field(empty_field)
field_3 = Field(empty_field)

# create crop instances
carrot = Crop("carrot", seedy_field, carrot_field_1, carrot_field_2, carrot_field_3, carrot_button_image, carrot_icon_image, 30, 70)

# create button instances
start_game_button = button.Button(500, 200, start_small, 1)
harvest_button_1 = button.Button(75, 285, harvest_small, 1)
harvest_button_2 = button.Button(450, 285, harvest_small, 1)
harvest_button_3 = button.Button(825, 285, harvest_small, 1)
carrot_button_1 = button.Button(75, 720, carrot.button, 1)
carrot_button_2 = button.Button(450, 720, carrot.button, 1)
carrot_button_3 = button.Button(825, 720, carrot.button, 1)

# timers
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 1000) # every 1000 milliseconds = every 1 second

# text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# game variables
page_state = "menu"
run = True
game_timer = 0
score = 0

while run:
    screen.blit(background_scaled, (0, 0))
    
    if(page_state == "menu"):
        if start_game_button.draw(screen):
            page_state = "fields"

    if(page_state == "fields"):
        background_scaled.blit(field_1.empty_field, (75, 400))
        background_scaled.blit(field_2.empty_field, (450, 400))
        background_scaled.blit(field_3.empty_field, (825, 400))
        background_scaled.blit(carrot.icon, (75, 808))
        draw_text(f"{carrot.get_crop_amount()}", font_1, text_colour_1, 150, 820)
        draw_text(f"Score: {score}", font_1, text_colour_1, 75, 50)

# carrot buttons
        if carrot_button_1.draw(screen):
            if field_1.get_crops_harvested() == True:
                field_1.set_crops_harvested(False)
                field_1.reset_growth_timer()
                field_1.set_active_growth(True)

        if carrot_button_2.draw(screen):
            if field_2.get_crops_harvested() == True:
                field_2.set_crops_harvested(False)
                field_2.reset_growth_timer()
                field_2.set_active_growth(True)

        if carrot_button_3.draw(screen):
            if field_3.get_crops_harvested() == True:
                field_3.set_crops_harvested(False)
                field_3.reset_growth_timer()
                field_3.set_active_growth(True)

# harvest buttons
        if harvest_button_1.draw(screen):
            if field_1.get_growth_timer() >= 4:
                field_1.set_crops_harvested(True)
                field_1.set_active_growth(False)
                field_1.reset_growth_timer()
                score += 1

        if harvest_button_2.draw(screen):
            if field_2.get_growth_timer() >= 4:
                field_2.set_crops_harvested(True)
                field_2.set_active_growth(False)
                field_2.reset_growth_timer()
                score += 1

        if harvest_button_3.draw(screen):
            if field_3.get_growth_timer() >= 4:
                field_3.set_crops_harvested(True)
                field_3.set_active_growth(False)
                field_3.reset_growth_timer()
                score += 1

# growth stages
        if not field_1.get_crops_harvested():
            if field_1.get_active_growth() and field_1.get_growth_timer() < 4:
                background_scaled.blit(carrot.seedling_list[field_1.get_growth_timer()], (75, 400))
            else:
                field_1.set_active_growth(False)
                background_scaled.blit(carrot.seedling_list[3], (75, 400))

        if not field_2.get_crops_harvested():
            if field_2.get_active_growth() and field_2.get_growth_timer() < 4:
                background_scaled.blit(carrot.seedling_list[field_2.get_growth_timer()], (450, 400))
            else:
                field_2.set_active_growth(False)
                background_scaled.blit(carrot.seedling_list[3], (450, 400))

        if not field_3.get_crops_harvested():
            if field_3.get_active_growth() and field_3.get_growth_timer() < 4:
                background_scaled.blit(carrot.seedling_list[field_3.get_growth_timer()], (825, 400))
            else:
                field_3.set_active_growth(False)
                background_scaled.blit(carrot.seedling_list[3], (825, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == TIMEREVENT and page_state == "fields":
            game_timer += 1
            field_1.increment_growth_timer()
            field_2.increment_growth_timer()
            field_3.increment_growth_timer()

    pygame.display.update()

pygame.quit()