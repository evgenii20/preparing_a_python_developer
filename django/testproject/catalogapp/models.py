# from django.db import models

# Create your models here.


# class ProductCatalog(models.Model):
#     """Модель каталог"""
#     name = models.CharField(max_length=64, verbose_name="Название товара")
#     dates = models.DateField(verbose_name="Дата поступления")
#     price = models.IntegerField(verbose_name="Цена", default=0)
#     # единица измерения - unit
#     unit = models.CharField(max_length=2, verbose_name="Единица измерения")
#     # name supplier - наименование поставщика
#     name_supplier = models.CharField(max_length=64, verbose_name="Наименование поставщика")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Карточка товара'
#         verbose_name_plural = 'Карточки товаров'
