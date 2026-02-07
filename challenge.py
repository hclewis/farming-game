import pygame
import random

vegetables = ["carrot", "beet", "cauli", "onion"]

class Challenge():
    def __init__(self,vegetables):
        self.vegetables = vegetables
        self.title = ""
    
    def gen_challenge(self):
        ran0 = random.randint(1,2)
        if ran0 == 1:
            ran1 = random.randint(6,10)
            veg1 = self.vegetables[random.randint(0,3)]
            self.title = f"Gather {ran1} {veg1}s"
        
        elif ran0 == 2:
            ran2 = random.randint(2,5)
            ran3 = random.randint(2,5)
            veg2 = self.vegetables[random.randint(0,3)]
            veg3 = self.vegetables[random.randint(0,3)]
            while veg2 == veg3:
                veg3pos = random.randint(0,3)
                veg3 = self.vegetables[veg3pos]
            self.title = f"Gather {ran2} {veg2}s and {ran3} {veg3}s"