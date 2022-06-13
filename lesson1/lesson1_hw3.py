"""
lesson 1: hw 3
Разработать целочисленный генератор случайных чисел. В функцию передавать начальную и
конечную границу диапазона генерации (выдавать значения из диапазона включая концы).
Заполнить этими данными словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”, а значене сгенеренное случайное число.  Вывести содержимое словаря.
(Усложненный вариант по желанию*): Не использовать стандартный модуль python random.

"""

from pprint import pprint


def get_num_generator(start, end):
    """Функция принимает начальную и конечную границу диапазона"""
    # Получаем список елементов
    num_list = list(range(start, end + 1))
    dicts = {}
    for i in num_list:
        # Получаем рандомное число
        rnd = (end - start) * i
        dicts.update({f'elem_{i}': rnd})
    # return num_list, dicts
    return dicts


if __name__ in '__main__':
    # gen_generator(start, end)
    pprint(get_num_generator(5, 10))
    # print(get_num_generator(5, 10))

"""
Результат:
{'elem_10': 50,
 'elem_5': 25,
 'elem_6': 30,
 'elem_7': 35,
 'elem_8': 40,
 'elem_9': 45}
"""


