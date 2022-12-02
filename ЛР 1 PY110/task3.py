def task() -> str:
    """
    Функция находит самое короткое слово в списке list_words.
    :return: самое короткое слово
    """
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return min(list_words, key=len)  # используй ключевую у функции min, по которой она долна определять минимальный элемент


if __name__ == "__main__":
    print(task())
