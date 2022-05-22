"""
lesson 2 hw 2
Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться,
что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным
переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    """Класс родитель. Содержит статическую информацию о товаре: название и цену"""

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        """Специальный метод геттер (получение данных)"""
        return self.__name

    @property
    def get_price(self):
        """Специальный метод геттер (получение данных)"""
        return self.__price


class ItemDiscountReport(ItemDiscount):
    """Класс дочерний содержит метод get_parent_data"""

    def get_parent_data(self):
        """Метод отображает информацию о товаре в одной строке"""
        print(f'Название товара: {self.get_name}, Цена товара: {self.get_price}')


if __name__ in "__main__":
    # Создание конструктора класса ItemDiscount
    item_discount = ItemDiscount('Процессор эльбрус', 100000)
    # Создание конструктора дочернего класса ItemDiscountReport
    item_discount_report = ItemDiscountReport(item_discount.get_name, item_discount.get_price)
    # Вызов метода дочернего класса
    item_discount_report.get_parent_data()

"""
Результат:
Название товара: Процессор эльбрус, Цена товара: 100000
"""