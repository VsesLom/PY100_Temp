def min_len_check(fn):
    # записать обертку для исходной функции
    def wrapper(words: str):
        if not isinstance(words, str):
            raise TypeError("Аргумент функции не является строкой")
        elif len(words) < 10:
            raise ValueError("Строка слишком короткая")
        else:
            result = fn(words)
        return result
    return wrapper


# задекорировать функцию
@ min_len_check
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо
    # some_func(5)  # TypeError("Аргумент не является строкой")
    some_func("Short str")  # ValueError("Строка слишком короткая")