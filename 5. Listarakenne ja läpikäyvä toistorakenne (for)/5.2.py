i = input("Anna luku")
numbers = []

while i != "":
    numbers.append(i)
    i = input("Anna luku")

numbers.sort(reverse=True)

print(numbers[0:5])
print(numbers)