list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# найти сумму, количество и среднее арифметическое уникальных чисел

uniq_list = set(list_)
print(sum(uniq_list))
print(len(uniq_list))
print(round(sum(uniq_list) / len(uniq_list), 5))
