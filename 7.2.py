def correct_sentence(text):
    # Убирает лишние пробелы по краям
    text = text.strip()

    # Делает первую букву заглавной
    text = text[0].upper() + text[1:]

    # Добавлят точку
    if not text.endswith('.'):
        text += '.'

    return text


# Тесты
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print(correct_sentence("greetings, friends"))   # Покажет исправленный текст
print(correct_sentence("hello"))                # Покажет исправленный текст
print(correct_sentence("Greetings. Friends"))   # Покажет исправленный текст
