# Generated by Django 5.0.1 on 2024-02-08 07:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='name', unique=True),
            preserve_default=False,
        ),
    ]