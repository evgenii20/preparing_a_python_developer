"""
lesson 3 hw 4
Написать программу, в которой реализовать две функции. В первой должен
создаваться простой текстовый файл. Если файл с таким именем уже существует,
выводим соответствующее сообщение и завершаем работу. Необходимо открыть файл
и создать два списка: с текстовой и числовой информацией. Для создания списков
использовать генераторы. Применить к спискам функцию zip(). Результат выполнения
этой функции должен должен быть обработан и записан в файл таким образом, чтобы
каждая строка файла содержала текстовое и числовое значение (например example345).
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл. Во
второй функции необходимо реализовать открытие файла и простой, построчный вывод
содержимого.

"""
import os
import random
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
            file.writelines([f'{text}{number}\n' for text, number in zip(strings, numbers)])
            return file.name


def read_file(sPath):
    """Чтение файла и вывод строк"""

    with open(sPath, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            print(line, end='')


if __name__ in '__main__':
    file = 'file4.txt'
    read = create_file(file)
    read_file(read)


"""
Результат:
ixyseyodzl9
dtrfmpahgv6
vzlbsclvgt76

"""
