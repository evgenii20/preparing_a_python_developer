from django.db import models

# Create your models here.
from catalogapp.models import ProductCatalog

from django.db.models import Manager


class DeletedQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(deleted=False)


class DeletedManager(Manager):
    # def get_queryset(self):
    #     return super().get_queryset().filter(deleted=False)

    def get_queryset(self):
        return DeletedQuerySet(self.model, using=self._db)

    def not_deleted(self):
        return self.get_queryset().not_deleted()


class Section(models.Model):
    """Модель раздела"""
    part_list = models.CharField(max_length=64, verbose_name="Раздел")
    # product_catalog = models.ForeignKey(ProductCatalog, on_delete=models.CASCADE, verbose_name="Раздел для пролуктов")
    # product_catalog = models.ManyToManyField(ProductCatalog, on_delete=models.CASCADE)
    product_catalog = models.ManyToManyField(ProductCatalog)
    deleted = models.BooleanField(default=False, null=False)
    objects = DeletedManager()

    def __str__(self):
        # return f'{self.part_list} {self.product_catalog.name}'
        return f'{self.part_list}'

    class Meta:
        verbose_name = 'Раздел товара'
        verbose_name_plural = 'Разделы товаров'
