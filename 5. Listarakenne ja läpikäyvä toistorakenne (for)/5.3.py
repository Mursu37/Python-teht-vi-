i = int(input("Anna kokonaisluku"))

for n in range(2, i):
    if i % n == 0:
        print("Ei ole alkuluku")
        break
else:
    print("On alkuluku")
