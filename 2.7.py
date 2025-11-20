num = input("Введіть 4-значне число: ")

# Перевірка на коректність довжини
if len(num) == 4 and num.isdigit():
    for digit in num:
        print(digit)
else:
    print("Потрібно ввести саме 4-значне число!")
