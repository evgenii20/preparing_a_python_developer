"""
lesson 2 hw 5
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс
ItemDiscountReport на два класса. Инициализировать классы необязательно. Внутри
каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод
названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info
"""


class ItemDiscount:
    """Класс родитель. Содержит статическую информацию о товаре: название и цену.
    Добавлены инкапсулированные свойства и методы работы с ними"""

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


class ItemDiscountReportInfoName(ItemDiscountReport):
    """Проверка на практике возможности полиморфизма. Класс с функцией 'get_info'
        отвечаетющей за вывод названия товара"""

    def get_info(self):
        print(self.get_name)


class ItemDiscountReportInfoPrice(ItemDiscountReport):
    """Проверка на практике возможности полиморфизма. Класс с функцией 'get_info'
            отвечаетющей за вывод цены товара"""

    def get_info(self):
        print(self.get_price)


if __name__ in "__main__":
    # Полиморфизм в методах классов
    first_info = ItemDiscountReportInfoName('Яблоки', 50000)
    second_info = ItemDiscountReportInfoPrice('Капуста', 70000)

    # for obj in (first_info, second_info):
    #     obj.get_info()
    #
    # print('-' * 5)

    # Полиморфизм в функциях
    def obj_handler(obj):
        """Функция обработчик. Принимает объект и вызывает метод 'get_info()' """
        obj.get_info()


    obj_handler(first_info)
    obj_handler(second_info)

"""
Результат:
Яблоки
70000
"""
