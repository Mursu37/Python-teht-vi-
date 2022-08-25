sukupuoli = input("Anna biologinen sukupuoli")
hemo = float(input("Anna hemoglobiiniarvo"))

if sukupuoli == "nainen" or sukupuoli == "Nainen":
    if hemo < 117:
        print("Alhainen hemoglobiiniarvot")
    elif hemo > 175:
        print("Korkeat hemoglobiiniarvot")
    else:
        print("Hemoglobiiniarvot normaalit")

if sukupuoli == "mies" or sukupuoli == "Mies":
    if hemo < 134:
        print("Alhainen hemoglobiiniarvot")
    elif hemo > 195:
        print("Korkeat hemoglobiiniarvot")
    else:
        print("Hemoglobiiniarvot normaalit")