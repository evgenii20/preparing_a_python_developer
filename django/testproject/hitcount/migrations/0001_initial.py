# Generated by Django 4.0.4 on 2022-06-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('path', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('hits', models.IntegerField(default=1)),
            ],
        ),
    ]
