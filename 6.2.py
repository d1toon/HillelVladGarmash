sec = int(input("Введіть кількість секунд: "))

days, remainder = divmod(sec, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

# Вибір правильного слова "день/дні"
if days % 10 == 1 and days % 100 != 11:
    d_word = "день"
else:
    d_word = "дні"

print(f"{days} {d_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
