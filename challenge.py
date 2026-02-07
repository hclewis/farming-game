import random

vegetables = ["carrot", "beet", "cauli", "onion"]

class Challenge():
    def __init__(self, vegetables):
        self.vegetables = vegetables
        self.title = ""
    
    def gen_challenge(self):
        ran0 = random.randint(1,2)
        if ran0 == 1:
            ran1 = random.randint(6,10)
            veg1 = self.vegetables[random.randint(0,3)]
            veg1.set_crop_amount_required(ran1)
            self.title = f"Gather {ran1} {veg1.name}s"
        
        elif ran0 == 2:
            ran2 = random.randint(2,5)
            ran3 = random.randint(2,5)
            veg2 = self.vegetables[random.randint(0,3)]
            veg3 = self.vegetables[random.randint(0,3)]
            while veg2 == veg3:
                veg3pos = random.randint(0,3)
                veg3 = self.vegetables[veg3pos]
            veg2.set_crop_amount_required(ran2)
            veg3.set_crop_amount_required(ran3)
            self.title = f"Gather {ran2} {veg2.name}s and {ran3} {veg3.name}s"

    def check_challenge_status(self):
        index = 0
        challenge_complete = self.vegetables[index].compare_crop_amount()
        index += 1
        while challenge_complete and index < len(vegetables):
            challenge_complete = self.vegetables[index].compare_crop_amount()
            index += 1

        if challenge_complete:
            for vegetable in self.vegetables:
                vegetable.reduce_crop_amount()
        
            self.gen_challenge()

        return challenge_complete