#inch = 2.54 cm
inch = float(input("tuumaa"))
inch_to_cm = 2.54
while inch >= 0:
    i = inch / inch_to_cm
    print(f"{inch:.2f} tuumaa on {i:.2f} senttimetriä")
    inch = float(input("tuumaa"))