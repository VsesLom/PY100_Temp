def delete(list_, index=None):  # реализовать функцию удаления элемента из списка по индексу
    if index is None:
        list_ = list_[:len(list_)-1]
    elif index == 0:
        list_ = list_[1:]
    else:
        add_list_1 = list_[:index]
        add_list_2 = list_[index+1:]
        list_ = add_list_1 + add_list_2

    return list_

print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
