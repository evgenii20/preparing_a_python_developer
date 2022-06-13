"""
lesson 2 hw 1
Создать два класса. Первый — родительский (ItemDiscount), должен содержать статическую
информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен
содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в
одной строке вида (“{название товара} {цена товара}”). Создать экземпляры родительского
класса и дочернего. Распечатать информацию о товаре.
"""


class ItemDiscount:
    """Класс родитель. Содержит статическую информацию о товаре: название и цену"""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    """Класс дочерний содержит метод get_parent_data"""

    def get_parent_data(self):
        """Метод отображает информацию о товаре в одной строке"""
        print(f'Название товара: {self.name}, Цена товара: {self.price}')


if __name__ in "__main__":
    # Создание конструктора класса ItemDiscount
    item_discount = ItemDiscount('Процессор эльбрус', 100000)
    # Создание конструктора дочернего класса ItemDiscountReport
    item_discount_report = ItemDiscountReport(item_discount.name, item_discount.price)
    # Вызов метода дочернего класса
    item_discount_report.get_parent_data()

"""
Результат:
Название товара: Процессор эльбрус, Цена товара: 100000
"""