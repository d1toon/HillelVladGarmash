while True:
    a = float(input("Введіть перше число: "))
    op = input("Введіть операцію (+, -, *, /): ")
    b = float(input("Введіть друге число: "))

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b == 0:
            print("Помилка: ділення на нуль!")
        else:
            print("Результат:", a / b)
    else:
        print("Невідома операція!")

    cont = input("Продовжити? (yes/y для продовження): ").lower()
    if cont not in ("yes", "y"):
        print("Роботу завершено.")
        break
