def task(camel_case_str: str) -> str:
    """
    Функция отфильтровывает из передаваемой строки только буквы нижнего регистра.
    :param camel_case_str: передаваемая строка
    :return: преобразованная строка
    """
    return "".join(filter(str.islower, camel_case_str))  # отфильтровать только буквы нижнего регистра


if __name__ == "__main__":
    word = "AbCdEfGh"
    print(task(word))
