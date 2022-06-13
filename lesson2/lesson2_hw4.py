"""
lesson 2 hw 4
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться
в качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора
дочернего класса (метод __init__, в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться
цена и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно,
не забудьте инициализировать дочерний и родительский классы (вторая и третья строка
после объявления дочернего класса).
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

    def set_price(self, value):
        """Специальный метод сеттер (установка данных)"""
        self.__price = value


class ItemDiscountReport(ItemDiscount):
    """Класс дочерний содержит метод get_parent_data"""

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        """Метод пересчёта цены товара по скидке и возврата результата в строке"""
        result = self.get_price - self.get_price * (self.discount / 100)
        return f'Цена товара со скидкой {self.discount}%: {result}'

    def get_parent_data(self):
        """Метод отображает информацию о товаре в одной строке"""
        print(f'Название товара: {self.get_name}, Цена товара: {self.get_price}')


if __name__ in "__main__":
    # Создание конструктора класса ItemDiscount
    item_discount = ItemDiscount('Процессор эльбрус', 100000)
    # Установка новой цены
    item_discount.set_price(60000)
    # # При использовании "@get_price.setter"
    # item_discount.set_price = 60000
    # Создание конструктора дочернего класса ItemDiscountReport
    item_discount_report = ItemDiscountReport(item_discount.get_name, item_discount.get_price, 40)
    # Вызов метода дочернего класса
    item_discount_report.get_parent_data()
    # Вывод преведения объекта к строке
    print(str(item_discount_report))


"""
Результат:
Название товара: Процессор эльбрус, Цена товара: 60000
Цена товара со скидкой 40%: 36000.0
"""