def sum_even_index(nums):
    if not nums:  # якщо список порожній
        return 0
    return sum(nums[0::2]) * nums[-1]  # сума елементів з парними індексами * останній елемент

# Приклад використання
numbers = [0, 1, 7, 2, 4, 8]
result = sum_even_index(numbers)
print(result)  # Виведе: 88

