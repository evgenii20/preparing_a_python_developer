"""
lesson 1: hw 2
Реализовать функцию print_directory_contents(path). Функция принимает имя
директории и выводит ее содержимое, включая содержимое всех
поддиректории (рекурсивно вызывая саму себя). Использовать os.walk нельзя,
но можно использовать os.listdir и os.path.isfile
"""

import os


def print_directory_contents(sPath):
    """Функция принимает имя директории и выводит ее содержимое"""

    for sSubDirectory in os.listdir(sPath):
        # объединяем путь и каталог/файл
        s_sub_directory_path = os.path.join(sPath, sSubDirectory)
        # Функция os.path.isdir() вернет True, если переданное имя ссылается на существующий каталог.
        if os.path.isdir(s_sub_directory_path):  # True
            # print('Каталог: ')
            print(s_sub_directory_path)
            # вызываем функцию ещё раз если мы в каталоге
            print_directory_contents(s_sub_directory_path)
        else:
            # Функция os.path.isfile() вернет True, если переданное имя ссылается на существующий файл.
            if os.path.isfile(s_sub_directory_path):  # True
                # print('файл: ')
                print(s_sub_directory_path)


if __name__ in "__main__":
    # вызов
    # print_directory_contents(".\\test1")
    print_directory_contents(".")

"""
Результат:
.\test1\sub_test1
.\test1\sub_test1\sub_test1.txt
.\test1\sub_test2
.\test1\sub_test2\sub_test2_f1.txt
.\test1\sub_test2\sub_test2_f2.txt
.\test1\test1.txt

"""
