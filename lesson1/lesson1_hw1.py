"""
lesson 1: hw 1
Вывести таблицу умножения в виде.
1 x 1 = 1
1 x 2 = 2
..
1 x 10 = 10
—
2 x 1 = 2
2 x 2 = 4
…
N x 10 = 10N

    Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию)
Между разделами вывести разделитель в виде 5 девисов

"""


def calc(multiplier1, multiplier2):
    """Функция принимает два параметра и умножает их. После блока выводим разделитель в виде 5 дефисов"""

    for el in range(1, multiplier1 + 1):
        for el2 in multiplier2:
            res = el * el2
            print(f'{el} x {el2} = {res}')
        print('-' * 5)


if __name__ in "__main__":
    # вызов
    # multiplier - множитель
    # multiplier1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # multiplier1 = []
    # multiplier1.append(int(input('Введите целое положительное число \nв диапазоне от 1 до 10:')))
    multiplier1 = int(input('Введите целое положительное число: '))
    multiplier2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    calc(multiplier1, multiplier2)
