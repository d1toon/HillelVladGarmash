def second_index(text, some_str):
    # находим первый индекс
    first = text.find(some_str)
    if first == -1:
        return None

    # Находим второй индекс
    second = text.find(some_str, first + len(some_str))

    if second == -1:
        return None

    return second

print(second_index("sims", "s"))            # 3
print(second_index("find the river", "e"))  # 12
print(second_index("hi", "h"))              # None
print(second_index("Hello, hello", "lo"))   # 10
