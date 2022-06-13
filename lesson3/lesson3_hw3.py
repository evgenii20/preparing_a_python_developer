"""
lesson 3 hw 3
Создать два списка с различным количеством элементов. В первом должны быть
записаны ключи, во втором — значения. Необходимо написать функцию, создающую
из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
для него должно сохраняться значение None. Если есть  значения, которым не
хватило ключей, их необходимо отбросить.

"""


def create_dict(my_list_key: list, my_list_value: list) -> dict:
    """Функция, создающая из данных 1-го списка ключи, из 2-го значения"""

    dict_number = {}
    for key in range(len(my_list_key)):
        # print(my_list_key[key])
        try:
            if my_list_value[key] != '':
                dict_number[my_list_key[key]] = my_list_value[key]
        except IndexError:
            dict_number[my_list_key[key]] = None

    return dict_number


if __name__ in '__main__':
    my_list = ['один', 'два', 'три', 'четыре', 'пять']
    # my_list_number = [1, 2, 3, 4, 5, 6, 7]
    my_list_number = [1, 2, 3]
    print(create_dict(my_list, my_list_number))

"""
Результат:
{'один': 1, 'два': 2, 'три': 3, 'четыре': None, 'пять': None}
"""
