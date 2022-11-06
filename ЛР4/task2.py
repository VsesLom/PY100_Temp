from random import randint
# написать функцию для получения списка уникальных целых чисел
def get_unique_list_numbers(minimum: int=-10, maximum: int=10, size: int=15) -> list[int]:
    """
    Функция, которая возвращает список, заполненный случайными уникальными целыми числами.
    :param minimum: минимум для диапазона случайных чисел (по умолчанию равен -10)
    :param maximum: максимум для диапазона случайных чисел (по умолчанию равен 10)
    :param size: длина возвращаемого списка
    :return: список из случайных уникальных целых чисел
    """
    unique_list = []
    while len(unique_list) < size:
        unique_num = randint(minimum, maximum)
        if unique_num not in unique_list:
            unique_list.append(unique_num)

    return unique_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
