"""
lesson 3 hw 5
Расширить программу из п. 4:
Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором
списке часть строковых значений (выбирается случайно) заменить на значения
типа 345example (в обратном порядке, число и строка). (То есть вы переделываете
функцию записи в файл так, чтобы она иногда меняла запись на 345example)
Реализовать функцию поиска определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.
Реализовать функцию замену всех найденных подстрок на новое значение и вывод
измененных строк. (это ДВЕ ОТДЕЛЬНЫЕ функции которые ВЫВОДЯТ значения, не записывают
и не модифицируют файлы)

"""
import os
import random
import re
import string

COUNT_SIZE = 10


def randomword():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(COUNT_SIZE))


def create_file(sPath):
    """Функция, создаёт простой файл и заполняет его текстовой и числовой информацией"""

    if os.path.isfile(sPath):
        return f'Файл {sPath} уже создан!'
    else:
        with open(sPath, 'w', encoding='UTF-8') as file:
            strings = [randomword() for el in range(COUNT_SIZE)]
            numbers = [random.randint(1, 100) for el in range(COUNT_SIZE)]
            # file.writelines([f'{number}{text}\n' for text, number in zip(strings, numbers)])
            count = 0
            for text, number in zip(strings, numbers):
                count += 1
                if count < 2:
                    file.writelines(f'{number}{text}\n')
                else:
                    file.writelines(f'{text}{number}\n')

            example_sub_str = random.choice(strings)
            return file.name, example_sub_str


def print_text(text, sub_str):
    """"""
    pattern = f'{sub_str}\d+'
    new_string = '1234asdf'
    # Вывод первого вхождения
    first = re.search(pattern, text)
    print(first)
    # Вывод всех вхождений
    alls = re.findall(pattern, text)
    print(alls)
    # замена всех найденных подстрок на новое значение
    text1 = (re.sub(pattern, new_string, text)).split('\n')

    for el in range(len(text1)):
        print(text1[el])

def read_file(sPath, sub_str):
    """Чтение файла и вывод строк"""

    with open(sPath, 'r', encoding='UTF-8') as file:
        text = file.read()
        print_text(text, sub_str)


if __name__ in '__main__':
    file = 'file5.txt'
    read, sub_str = create_file(file)
    read_file(read, sub_str)

"""
Результат:
['vkdgtwzwcs17']
57mimyqvfmqk
bpnxglbqdd21
hfbpxzgjyp35
tipapdxwxl34
idcgytwdul14
txzkalwumc36
zbdymbicos43
crubxjrunp21
1234asdf
lrxdfuybdz34
"""
