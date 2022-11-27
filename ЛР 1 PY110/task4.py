def list_comprehension(words: list) -> list:
    """
    Функция переводит первую букву каждого слова списка в верхний регистр, а остальные - в нижний.
    :param words: передаваемый список слов
    :return: преобразованный список слов
    """
    return [val.capitalize() for val in words]  #


def list_map(words: list) -> list:
    """
    Функция переводит первую букву каждого слова списка в верхний регистр, а остальные - в нижний.
    :param words: передаваемый список слов
    :return: преобразованный список слов
    """
    return list(map(str.capitalize, words))  #


def task():
    list_words = [
        "goldenROD",
        "puRPle",
        "sAlMoN",
        "TURQUOISE",
        "cYAN"
    ]

    print(list_comprehension(list_words))
    print(list_map(list_words))


if __name__ == "__main__":
    task()
