from django.db import models

# Create your models here.
# from catalogapp.models import Section
from django.db.models import Manager


class DeletedQuerySet(models.QuerySet):
    """Добавляем в QuerySet ещё один фильтр not_deleted"""
    def not_deleted(self):
        return self.filter(deleted=False)


class DeletedManager(Manager):
    """Кастомный менеджер, нужно чтоб возвращался не базовый querySet, а что мы создали"""
    # def get_queryset(self):
    #     """Переопределяем get_queryset"""
    #     qs = super().get_queryset()
    #     # qs = qs.filter(deleted=False)
    #     # qs = super().get_queryset().filter(deleted=False) # всё в одну, либо сразу вернуть
    #     return qs
    # ---
    # def get_queryset(self):
    #     return super().get_queryset().filter(deleted=False)

    def get_queryset(self):
        """Переопределяем queryset особым вызовом. Передаём модель и подключение к БД
        в приватной переменной"""
        return DeletedQuerySet(self.model, using=self._db)

    def not_deleted(self):
        return self.get_queryset().not_deleted()


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

    # new string 1ч 19 мин
    deleted = models.BooleanField(default=False, null=False)
    objects = DeletedManager()

    def __str__(self):
        unit_choice_names = {"P": "шт",
                             "K": "кг"}
        return f'{self.name} {unit_choice_names[self.unit]}'

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'
