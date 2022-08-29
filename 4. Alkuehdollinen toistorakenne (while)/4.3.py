n = input("Anna luku")
smallest = float(n)
biggest = float(n)
while n != "":
    n = float(n)
    if n < smallest:
        smallest = n
    if n > biggest:
        biggest = n
    n = input("Anna luku")

print(f"Pienin luku {smallest} \nIsoin luku {biggest}")