from itertools import cycle


def task() -> None:
    """
    Функция печатает в столбик первые 10 элементов итератора cycle из кортежа a.
    :return: None
    """
    a = (1, 2, 3)
    repeater = cycle(a)  # бесконечно повторяем элементы кортежа
    for _ in range(10):
        print(next(repeater))


if __name__ == "__main__":
    task()
