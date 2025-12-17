def add_one(some_list):
    i = len(some_list) - 1

    while i >= 0:
        if some_list[i] < 9:
            some_list[i] += 1
            return some_list
        some_list[i] = 0
        i -= 1

    return [1] + some_list


print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))