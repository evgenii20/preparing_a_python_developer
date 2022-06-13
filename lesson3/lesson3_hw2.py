"""
lesson 3 hw 2
Написать программу, которая запрашивает у пользователя ввод числа. На введенное
число она отвечает сообщением, целое оно или дробное. Если дробное — необходимо
далее выполнить сравнение чисел до и после запятой. Если они совпадают, программа
должна возвращать значение True, иначе False.

"""


def check(s: str):
    """Функция проверки на целое и дробное число"""
    try:
        if int(s):
            print('Целое число')
    except ValueError:
        try:
            left, right = s.split('.')
            l, r = int(left), int(right)
            if type(l) == type(r):
                print('Дробное число')
        except ValueError:
            print('Не число')


if __name__ in '__main__':
    check_number = input('Введите число, например: "123" или "12.3": ')
    # check_number = '12.3'
    # check_number = '12.e'
    print(check(check_number))

"""
Результат:
Введите число, например: "123" или "12.3": 123
Целое число
--
Введите число, например: "123" или "12.3": 12.3
Дробное число
"""
