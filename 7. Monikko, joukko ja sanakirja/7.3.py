airports = {"EFHK":"Helsinki-Vantaan lentokenttä",
            "EFKS":"Kuusamon lentokenttä",
            "EFTU":"Turun lentokenttä"
            }
def new_airport(icao, name):
    airports[icao] = name

print("Toiminnot ovat \"haku\", \"uusi\", \"lopeta\".")
user = input("Mitä haluat tehdä?").lower()

while user != "lopeta":
    if user == "uusi":
        code = input("Anna lentokentän ICAO-koodi").upper()
        location = input("Anna lentokentän nimi")
        new_airport(code, location)
    elif user == "haku":
        code = input("Anna lentokentän ICAO-koodi").upper()
        print(airports[code])
    user = input("Mitä haluat tehdä").lower()