import random
dice = 0
count = 0

def dice_throw():
    return random.randint(1, 6)

while dice < 6:
    dice = dice_throw()
    count += 1
    print(dice)

print(f"{count} heittoa")