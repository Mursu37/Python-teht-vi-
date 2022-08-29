import random
n = random.randint(1, 10)
guess = int(input("Anna numero yhden ja kymmenen väliltä: "))

while guess != n:
    if guess > n:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")
    guess = int(input("Anna uusi numero: "))

print("Oikein")