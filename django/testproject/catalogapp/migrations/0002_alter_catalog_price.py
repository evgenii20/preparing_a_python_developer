# Generated by Django 4.0.4 on 2022-05-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]