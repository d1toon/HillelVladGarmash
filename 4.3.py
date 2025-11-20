import random

size = random.randint(3, 10)
random_list = [random.randint(0, 10) for _ in range(size)]
print("Випадковий список:", random_list)

if len(random_list) >= 3:
    new_list = [random_list[0], random_list[2], random_list[-2]]
    print("Фінальний список:", new_list)
else:
    print("Список занадто короткий для вибору трьох елементів")
