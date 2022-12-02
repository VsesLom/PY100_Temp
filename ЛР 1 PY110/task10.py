def task() -> None:
    """
    Функция объединяет списки numbers, chars поэлементно и печатает результат в столбик.
    :return: None
    """
    numbers = [1, 2, 3, 4, 5]
    chars = ["a", "b", "c", "d", "e"]
    for number, char in zip(numbers, chars):  # поэлементно объединить numbers и chars
        print(f"{number}-{char}")


if __name__ == "__main__":
    task()
