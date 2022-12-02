from itertools import repeat


def task() -> None:
    """
    Функция печатает в столбик переменную a 4 раза.
    :return: None
    """
    a = 10
    for num in repeat(a, 4):  # повторить переменную a 4 раза
        print(num)


if __name__ == "__main__":
    task()
