import string
import keyword


def is_valid_variable_name(name: str) -> bool:
    # Перевірка на порожній рядок
    if not name:
        return False

    # Перевірка на початок з цифри
    if name[0].isdigit():
        return False

    # Перевірка на наявність великих літер
    if any(c.isupper() for c in name):
        return False

    # Перевірка на пробіли або небажані символи
    allowed_chars = string.ascii_lowercase + string.digits + "_"
    if any(c not in allowed_chars for c in name):
        return False

    # Перевірка кількості нижніх підкреслень
    if name.count("_") > 1:
        return False

    # Перевірка на зарезервовані слова
    if name in keyword.kwlist:
        return False

    return True


# Приклади перевірки
test_names = ["_", "__", "___", "x", "get_value", "get value", "get!value",
              "some_super_puper_value", "Get_value", "get_Value", "getValue",
              "3m", "m3", "assert", "assert_exception"]

for name in test_names:
    print(name, "=>", is_valid_variable_name(name))
