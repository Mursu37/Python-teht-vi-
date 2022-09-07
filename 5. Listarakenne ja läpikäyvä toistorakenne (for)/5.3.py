i = int(input("Anna kokonaisluku"))

for n in range(2, i):
    print(n)
    if i % n == 0:
        print("Ei ole alkuluku")
        break
else:
    print("On alkuluku")
