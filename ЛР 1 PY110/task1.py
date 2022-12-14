def task() -> list:
    """
    Функция приводит к типу int каждый элемент списка num_list и возвращает список целых чисел.
    :return: список целых чисел
    """
    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,  # шестнадцатеричное представление
        0b1010101010  # бинарное представление представление
    ]

    return list(map(int, num_list))  # c помощью функции map привести каждый элемент списка к типу int


if __name__ == "__main__":
    print(task())
