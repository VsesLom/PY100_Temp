list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# вышеуказанный список состоит из 20 элементов TODO поменять условие задания (в задании говориться про 10 элементов)
max_value = list_numbers[0]  # Оформить решение
max_index = 0

for index, value in enumerate(list_numbers):
    if value > max_value:
        max_value = value
        max_index = index

list_numbers[-1], list_numbers[max_index] = list_numbers[max_index], list_numbers[-1]
print(list_numbers)
