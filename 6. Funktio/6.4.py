def calculate_sum(array):
    total = 0
    for i in array:
        total += i
    return total

a = [1,2,3,5]
b = [10, 15, 20]
print(calculate_sum(a))
print(calculate_sum(b))