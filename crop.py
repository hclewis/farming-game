import pygame

class Crop():
    def __init__(self, name, seedy_field, field_1, field_2, field_3, button, icon, icon_width, icon_height, value):
        self.name = name
        self.crop_amount = 0
        self.crop_amount_required = 0
        self.seedy_field = pygame.transform.scale(seedy_field, (300,300))
        self.field_1 = pygame.transform.scale(field_1, (300,300))
        self.field_2 = pygame.transform.scale(field_2, (300,300))
        self.field_3 = pygame.transform.scale(field_3, (300,300))
        self.button = pygame.transform.scale(button, (70,70))
        self.icon = pygame.transform.scale(icon, (icon_width,icon_height))
        self.seedling_list = [self.seedy_field, self.field_1, self.field_2, self.field_3]
        self.value = value

    def increment_crop_amount(self):
        self.crop_amount += 1

    def get_crop_amount(self):
        return self.crop_amount
    
    def set_crop_amount_required(self, veg_num):
        self.crop_amount_required = veg_num

    def get_crop_amount_required(self):
        return self.crop_amount_required
    
    def compare_crop_amount(self):
        if self.crop_amount >= self.crop_amount_required:
            return True
        else:
            return False
        
    def reduce_crop_amount(self):
        self.crop_amount = self.crop_amount - self.crop_amount_required

    def reset_crop_amount(self):
        self.crop_amount_required = 0

    def get_crop_score(self):
        return self.value * self.crop_amount_required