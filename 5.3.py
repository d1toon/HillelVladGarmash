import string

text = input()


def make_hashtag(text):
    # Видаляємо усі знаки пунктуації та пробіли
    clean = ''.join(c for c in text if c.isalnum())

    # Розбиваємо на слова за допомогою пробілів у вихідному рядку
    words = text.split()

    # Робимо кожне слово з великої літери
    words = [w.capitalize() for w in words]

    # Об'єднуємо слова без пробілів і ставимо #
    hashtag = "#" + "".join(words)

    # Обрізаємо до 140 символів
    return hashtag[:140]


print(make_hashtag(text))
