def common_elements():
    # Список чисел  до 99 кратных 3
    list3 = [i for i in range(100) if i % 3 == 0]
    print("Числа, кратные 3:", list3)

    # Список чисел до 99 кратных 5
    list5 = [i for i in range(100) if i % 5 == 0]
    print("Числа, кратные 5:", list5)

    # Пересечение
    common_set = set(list3) & set(list5)
    print("Общие числа (пересечение):", common_set)

    return common_set
result = common_elements()
assert result == {0, 15, 30, 45, 60, 75, 90}
