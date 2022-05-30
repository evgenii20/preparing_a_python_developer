# Generated by Django 4.0.4 on 2022-05-29 15:40

from django.db import migrations


def forward(app, se):
    ProductCatalog = app.get_model('catalogapp', 'ProductCatalog')
    alias = se.connection.alias
    ProductCatalog.objects.using(alias).bulk_create([
        ProductCatalog(name='Куртка', price=150, unit='шт', name_supplier='ООО Куртка опт'),
        ProductCatalog(name='Джинсы', price=200, unit='шт', name_supplier='ООО Джинсы')
    ])


def revers(app, se):
    ProductCatalog = app.get_model('catalogapp', 'ProductCatalog')
    alias = se.connection.alias
    ProductCatalog.objects.using(alias).all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('catalogapp', '0002_alter_catalog_price'),
    ]

    operations = [
        migrations.RunPython(code=forward, reverse_code=revers)
        # Для БД не по умолчанию, настр. БД в settings
        # migrations.RunPython(code=forward, reverse_code=revers, hints=('target_db', 'other'))
    ]
