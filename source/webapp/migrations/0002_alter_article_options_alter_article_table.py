# Generated by Django 4.2.3 on 2023-08-03 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья'},
        ),
        migrations.AlterModelTable(
            name='article',
            table='articles',
        ),
    ]
