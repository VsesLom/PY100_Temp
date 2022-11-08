from random import sample
from string import ascii_letters, digits

# написать функцию генерации случайных паролей
def get_random_password(n: int=8) -> str:
    """
    Функция для генерации случайных паролей заданной длины n.
    :param n: длина пароля (по умолчанию равна 8)
    :return: пароль заданной длины
    """
    password_list = sample(ascii_letters + digits, n)
    password = ''
    for value in password_list:
        password += value
    return password


print(get_random_password())
