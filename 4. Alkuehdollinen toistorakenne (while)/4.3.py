n = input("Anna luku")
minValue = float(n)
maxValue = float(n)
while n != "":
    n = float(n)
    if n < minValue:
        minValue = n
    if n > maxValue:
        maxValue = n
    n = input("Anna luku")

print(f"Pienin luku {minValue} \nIsoin luku {maxValue}")