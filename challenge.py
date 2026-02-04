import random

vegetables = ["carrot", "beet", "cauli", "onion"]

def gen_challenge(vegetables):
    ran1 = random.randint(1,2)
    if ran1 == 1:
        ran2 = random.randint(6,10)
        veg1 = vegetables[random.randint(0,3)]
        return f"Gather {ran2} {veg1}s."
    elif ran1 == 2:
        ran3 = random.randint(2,5)
        ran4 = random.randint(2,5)
        veg2 = vegetables[random.randint(0,3)]
        veg3 = vegetables[random.randint(0,3)]
        while veg2 == veg3:
            veg3pos = random.randint(0,3)
            veg3 = vegetables[veg3pos]
        return f"Gather {ran3} {veg2}s and {ran4} {veg3}s"