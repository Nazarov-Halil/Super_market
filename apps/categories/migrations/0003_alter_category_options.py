# Generated by Django 5.0.1 on 2024-02-11 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]