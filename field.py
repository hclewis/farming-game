import pygame

class Field():
    def __init__(self, empty_field):
        self.empty_field = pygame.transform.scale(empty_field, (300, 300))