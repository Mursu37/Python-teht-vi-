name = "Mursu"
password = "Hunter2"
n = 0

name_input = input("Anna käyttäjätunnus")
password_input = input("Anna salasana")

while name_input != name or password_input != password:
    print("Pääsy evätty")
    n += 1
    if n >= 5:
        print("Liian monta yritystä")
        break
    name_input = input("Anna käyttäjätunnus")
    password_input = input("Anna salasana")

if name_input == name and password_input == password:
    print("Tervetuloa")