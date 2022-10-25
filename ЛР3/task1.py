main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def get_count_char(str_):  # посчитать количество каждой буквы в строке в аргументе str_
    low_str = str_.lower()
    dict_char = dict()
    for i in low_str:
        if i.isalpha():
            dict_char[i] = dict_char.get(i, 0) + 1

    return dict_char

print(get_count_char(main_str))

def percent_of_chars(dict_char):
    sum_values = 0
    for i in dict_char:
        sum_values += dict_char[i]
    for i in dict_char:
        dict_char[i] = round(dict_char[i] * 100 / sum_values, 2)
    return dict_char

print(percent_of_chars(get_count_char(main_str)))
