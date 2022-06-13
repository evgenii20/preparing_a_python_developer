"""
lesson 3 hw 1
Написать программу, которая будет содержать функцию для получения имени
файла из полного пути до него. При вызове функции в качестве аргумента
должно передаваться путь и имя файла с расширением. В функции необходимо
реализовать поиск имени файла (с расширением), а затем «выделение» имени
файла (без расширения). Расширений может быть несколько
(например testfile.tar.gz)

 posixpath for UNIX-style paths

 ntpath for Windows paths

"""

import os

def get_file_names(sPath:str) -> str:
    """Функция для получения имени файла из полного пути до него."""
    # Получаем абсолютный путь до файла
    abs_path_file = os.path.abspath(sPath)
    # C:\git-project\preparing_a_python_developer\lesson3\file1.txt
    # Поиск имени файла с расширением
    # # 1-й вариант:
    # name = os.path.basename(abs_path_file)
    # # file1.txt
    # index = name.index('.')
    # file_name = name[:index]
    # # /1-й вариант
    # 2-й вариант:
    file_with_extension = abs_path_file.split('\\')[-1]
    index = file_with_extension.index('.')
    file_name = file_with_extension[:index]

    # return f'Имя файла с расширением: "{name}"\nИмя файла без расширения: "{file_name}"'
    return f'Имя файла с расширением: "{file_with_extension}"\nИмя файла без расширения: "{file_name}"'


if __name__ in '__main__':
    print(get_file_names('file1.txt'))
    print('-' * 5)
    print(get_file_names('file2.txt.tar'))

"""
Результат:
Имя файла с расширением: "file1.txt"
Имя файла без расширения: "file1"
-----
Имя файла с расширением: "file2.txt.tar"
Имя файла без расширения: "file2"
"""