i = float(input("Anna galloona määrä"))

def gallon_to_liter(n):
    n = n * 3.785
    return n

while i >= 0:
    print(gallon_to_liter(i))
    i = float(input("Anna galloona määrä"))