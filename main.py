import pygame
import button
from crop import Crop
from field import Field
from challenge import Challenge

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Farming Game")

# colours
text_colour_1 = (255,255,255)

# fonts
font_1 = pygame.font.SysFont("arialblack", 40)

# game variables
page_state = "menu"
run = True
game_timer = 60
score = 0

# loading images
background = pygame.image.load('./images/background.png')
start = pygame.image.load("./images/buttons/start-button.png").convert_alpha()
harvest = pygame.image.load("./images/buttons/harvest-button.png").convert_alpha()
empty_field = pygame.image.load("./images/empty-field.png").convert_alpha()
seedy_field = pygame.image.load("./images/seedy-field.png").convert_alpha()
# carrots
carrot_field_1 = pygame.image.load("./images/carrot/carrot-field-1.png").convert_alpha()
carrot_field_2 = pygame.image.load("./images/carrot/carrot-field-2.png").convert_alpha()
carrot_field_3 = pygame.image.load("./images/carrot/carrot-field-3.png").convert_alpha()
carrot_button_image = pygame.image.load("./images/carrot/carrot-button.png").convert_alpha()
carrot_icon_image = pygame.image.load("./images/carrot/carrot-icon.png").convert_alpha()
# beetroots
beet_field_1 = pygame.image.load("./images/beet/beet-field-1.png").convert_alpha()
beet_field_2 = pygame.image.load("./images/beet/beet-field-2.png").convert_alpha()
beet_field_3 = pygame.image.load("./images/beet/beet-field-3.png").convert_alpha()
beet_button_image = pygame.image.load("./images/beet/beet-button.png").convert_alpha()
beet_icon_image = pygame.image.load("./images/beet/beet-icon.png").convert_alpha()
# cauliflowers
cauli_field_1 = pygame.image.load("./images/cauli/cauli-field-1.png").convert_alpha()
cauli_field_2 = pygame.image.load("./images/cauli/cauli-field-2.png").convert_alpha()
cauli_field_3 = pygame.image.load("./images/cauli/cauli-field-3.png").convert_alpha()
cauli_button_image = pygame.image.load("./images/cauli/cauli-button.png").convert_alpha()
cauli_icon_image = pygame.image.load("./images/cauli/cauli-icon.png").convert_alpha()
# onions
onion_field_1 = pygame.image.load("./images/onion/onion-field-1.png").convert_alpha()
onion_field_2 = pygame.image.load("./images/onion/onion-field-2.png").convert_alpha()
onion_field_3 = pygame.image.load("./images/onion/onion-field-3.png").convert_alpha()
onion_button_image = pygame.image.load("./images/onion/onion-button.png").convert_alpha()
onion_icon_image = pygame.image.load("./images/onion/onion-icon.png").convert_alpha()

# scale images
background_scaled = pygame.transform.scale(background, (1200, 900))
start_small = pygame.transform.scale(start, (200, 100))
harvest_small = pygame.transform.scale(harvest, (300, 90))

# create crop instances
carrot = Crop("carrot", seedy_field, carrot_field_1, carrot_field_2, carrot_field_3, carrot_button_image, carrot_icon_image, 20, 70, 3, 1)
beet = Crop("beet", seedy_field, beet_field_1, beet_field_2, beet_field_3, beet_button_image, beet_icon_image, 40, 70, 5, 0.6)
cauli = Crop("cauli", seedy_field, cauli_field_1, cauli_field_2, cauli_field_3, cauli_button_image, cauli_icon_image, 60, 45, 6, 0.4)
onion = Crop("onion", seedy_field, onion_field_1, onion_field_2, onion_field_3, onion_button_image, onion_icon_image, 30, 70, 4, 0.8)

# create button instances
start_game_button = button.Button(500, 200, start_small, 1)
harvest_button_1 = button.Button(75, 285, harvest_small, 1)
harvest_button_2 = button.Button(450, 285, harvest_small, 1)
harvest_button_3 = button.Button(825, 285, harvest_small, 1)
carrot_button_1 = button.Button(75, 720, carrot.button, 1)
carrot_button_2 = button.Button(450, 720, carrot.button, 1)
carrot_button_3 = button.Button(825, 720, carrot.button, 1)
beet_button_1 = button.Button(152, 720, beet.button, 1)
beet_button_2 = button.Button(526, 720, beet.button, 1)
beet_button_3 = button.Button(901, 720, beet.button, 1)
cauli_button_1 = button.Button(229, 720, cauli.button, 1)
cauli_button_2 = button.Button(603, 720, cauli.button, 1)
cauli_button_3 = button.Button(978, 720, cauli.button, 1)
onion_button_1 = button.Button(305, 720, onion.button, 1)
onion_button_2 = button.Button(680, 720, onion.button, 1)
onion_button_3 = button.Button(1055, 720, onion.button, 1)

# create challenge instance
quest = Challenge([carrot, beet, cauli, onion])

# timers
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 1000) # every 1000 milliseconds = every 1 second

# text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# create field instances
field_1 = Field(empty_field, [carrot, beet, cauli, onion])
field_2 = Field(empty_field, [carrot, beet, cauli, onion])
field_3 = Field(empty_field, [carrot, beet, cauli, onion])

# more variables
quest.gen_challenge()

# main game loop
while run:
    screen.blit(background_scaled, (0, 0))
    
    if(page_state == "menu"):
        if start_game_button.draw(screen):
            #
            page_state = "fields"

    if page_state == "end":
        screen.blit(background_scaled, (0, 0))
        draw_text("end game", font_1, text_colour_1, 75, 50)

    if(page_state == "fields"):
        screen.blit(field_1.empty_field, (75, 400))
        screen.blit(field_2.empty_field, (450, 400))
        screen.blit(field_3.empty_field, (825, 400))

        screen.blit(carrot.icon, (75, 808))
        draw_text(f"{carrot.get_crop_amount()}", font_1, text_colour_1, 150, 820)
        screen.blit(beet.icon, (325, 808))
        draw_text(f"{beet.get_crop_amount()}", font_1, text_colour_1, 400, 820)
        screen.blit(cauli.icon, (575, 808))
        draw_text(f"{cauli.get_crop_amount()}", font_1, text_colour_1, 650, 820)
        screen.blit(onion.icon, (825, 808))
        draw_text(f"{onion.get_crop_amount()}", font_1, text_colour_1, 900, 820)

        draw_text(f"Score: {score}", font_1, text_colour_1, 75, 50)
        draw_text(f"{quest.title}", font_1, text_colour_1, 400, 50)
        draw_text(f"{game_timer}", font_1, text_colour_1, 1000, 50)


# carrot buttons
        if carrot_button_1.draw(screen):
            if field_1.get_crops_harvested() == True:
                field_1.grow_crop("carrot")
        if carrot_button_2.draw(screen):
            if field_2.get_crops_harvested() == True:
                field_2.grow_crop("carrot")
        if carrot_button_3.draw(screen):
            if field_3.get_crops_harvested() == True:
                field_3.grow_crop("carrot")

# beet buttons
        if beet_button_1.draw(screen):
            if field_1.get_crops_harvested() == True:
                field_1.grow_crop("beet")
        if beet_button_2.draw(screen):
            if field_2.get_crops_harvested() == True:
                field_2.grow_crop("beet")
        if beet_button_3.draw(screen):
            if field_3.get_crops_harvested() == True:
                field_3.grow_crop("beet")

# cauli buttons
        if cauli_button_1.draw(screen):
            if field_1.get_crops_harvested() == True:
                field_1.grow_crop("cauli")
        if cauli_button_2.draw(screen):
            if field_2.get_crops_harvested() == True:
                field_2.grow_crop("cauli")
        if cauli_button_3.draw(screen):
            if field_3.get_crops_harvested() == True:
                field_3.grow_crop("cauli")

# onion buttons
        if onion_button_1.draw(screen):
            if field_1.get_crops_harvested() == True:
                field_1.grow_crop("onion")
        if onion_button_2.draw(screen):
            if field_2.get_crops_harvested() == True:
                field_2.grow_crop("onion")
        if onion_button_3.draw(screen):
            if field_3.get_crops_harvested() == True:
                field_3.grow_crop("onion")

# harvest buttons

        if harvest_button_1.draw(screen):
            if field_1.get_growth_timer() > 2:
                field_1.harvest_crop()
                quest.check_challenge_status()
                score = score + quest.current_score
                quest.reset_current_score()

        if harvest_button_2.draw(screen):
            if field_2.get_growth_timer() > 2:
                field_2.harvest_crop()
                quest.check_challenge_status()
                score = score + quest.current_score
                quest.reset_current_score()

        if harvest_button_3.draw(screen):
            if field_3.get_growth_timer() > 2:
                field_3.harvest_crop()
                quest.check_challenge_status()
                score = score + quest.current_score
                quest.reset_current_score()

# growth stages
        if not field_1.get_crops_harvested():
            if field_1.get_active_growth() and field_1.get_growth_timer() < 3:
                screen.blit(field_1.get_crop_img_list()[int(field_1.get_growth_timer())], (75, 400))
            else:
                field_1.set_active_growth(False)
                screen.blit(field_1.get_crop_img_list()[3], (75, 400))

        if not field_2.get_crops_harvested():
            if field_2.get_active_growth() and field_2.get_growth_timer() < 3:
                screen.blit(field_2.get_crop_img_list()[int(field_2.get_growth_timer())], (450, 400))
            else:
                field_2.set_active_growth(False)
                screen.blit(field_2.get_crop_img_list()[3], (450, 400))

        if not field_3.get_crops_harvested():
            if field_3.get_active_growth() and field_3.get_growth_timer() < 3:
                screen.blit(field_3.get_crop_img_list()[int(field_3.get_growth_timer())], (825, 400))
            else:
                field_3.set_active_growth(False)
                screen.blit(field_3.get_crop_img_list()[3], (825, 400))

        if game_timer == 0:
            page_state = "end"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == TIMEREVENT and page_state == "fields":
            game_timer -= 1
            field_1.increment_growth_timer()
            field_2.increment_growth_timer()
            field_3.increment_growth_timer()

    pygame.display.update()

pygame.quit()