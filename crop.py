import pygame

class Crop():
    def __init__(self, name, seedy_field, field_1, field_2, field_3, button, icon, x, y):
        self.name = name
        self.crop_amount = 0
        self.seedy_field = pygame.transform.scale(seedy_field, (300,300))
        self.field_1 = pygame.transform.scale(field_1, (300,300))
        self.field_2 = pygame.transform.scale(field_2, (300,300))
        self.field_3 = pygame.transform.scale(field_3, (300,300))
        self.button = pygame.transform.scale(button, (70,70))
        self.icon = pygame.transform.scale(icon, (x,y))
        self.seedling_list = [self.seedy_field, self.field_1, self.field_2, self.field_3]

    def increment_crop_amount(self):
        self.crop_amount += 1

    def get_crop_amount(self):
        return self.crop_amount