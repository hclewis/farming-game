import pygame

class Field():
    def __init__(self, empty_field):
        self.empty_field = pygame.transform.scale(empty_field, (300, 300))
        self.crops_harvested = True

    def set_crops_harvested(self, bool):
        self.crops_harvested = bool

    def get_crops_harvested(self):
        return self.crops_harvested