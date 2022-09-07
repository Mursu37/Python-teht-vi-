def filter(array):
    new_arr = array.copy()
    for i in new_arr:
        if i % 2 == 1:
            new_arr.remove(i)
    return new_arr

a = [1, 2, 3, 4, 7, 8]
print(filter(a))
print(a)