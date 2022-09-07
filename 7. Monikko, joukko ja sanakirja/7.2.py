names = set()
name = input("Anna nimi")

while name != "":
    if name in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.add(name)
    name = input("Anna nimi")

for i in names:
    print(i)