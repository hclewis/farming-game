import pygame

class Field():
    def __init__(self, empty_field, vegetables):
        self.empty_field = pygame.transform.scale(empty_field, (300, 300))
        self.crops_harvested = True
        self.growth_timer = 0
        self.active_growth = False
        self.current_crop = ""
        self.vegetables = vegetables

    def set_crops_harvested(self, bool):
        self.crops_harvested = bool

    def get_crops_harvested(self):
        return self.crops_harvested
    
    def increment_growth_timer(self):
        self.growth_timer += 1

    def reset_growth_timer(self):
        self.growth_timer = 0

    def get_growth_timer(self):
        return self.growth_timer
    
    def set_active_growth(self, bool):
        self.active_growth = bool

    def get_active_growth(self):
        return self.active_growth
    
    def set_current_crop(self, crop):
        self.current_crop = crop

    def get_current_crop(self):
        return self.current_crop
    
    def get_crop_img_list(self):
        for vegetable in self.vegetables:
            if vegetable.name == self.current_crop:
                return vegetable.seedling_list
            
    def increment_current_crop(self):
        for vegetable in self.vegetables:
            if vegetable.name == self.current_crop:
                vegetable.increment_crop_amount()