import random
i = int(input("Anna noppien määrä"))
sum = 0

for n in range(i):
    sum += random.randint(1, 6)

print(sum)