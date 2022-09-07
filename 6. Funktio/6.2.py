import random
dice = 0
count = 0
i = int(input("Anna numero"))
def dice_throw(max):
    return random.randint(1, max)

while dice < i:
    dice = dice_throw(i)
    count += 1
    print(dice)

print(f"{count} heittoa")