from django.db import models

# Create your models here.
# from catalogapp.models import Section


class ProductCatalog(models.Model):
    """Модель каталог"""

    PIECES = 'P'
    KILOGRAM = 'K'

    UNIT_CHOICES = (
        (PIECES, 'шт'),
        (KILOGRAM, 'кг'),
    )

    name = models.CharField(max_length=64, verbose_name="Название товара")
    dates = models.DateField(verbose_name="Дата поступления")
    price = models.IntegerField(verbose_name="Цена", default=0)
    # единица измерения - unit
    unit = models.CharField(max_length=1, choices=UNIT_CHOICES, verbose_name="Единица измерения")
    # name supplier - наименование поставщика
    name_supplier = models.CharField(max_length=64, verbose_name="Наименование поставщика")
    # partition = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Раздел")

    def __str__(self):
        unit_choice_names = {"P": "шт",
                             "K": "кг"}
        return f'{self.name} {unit_choice_names[self.unit]}'

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'
