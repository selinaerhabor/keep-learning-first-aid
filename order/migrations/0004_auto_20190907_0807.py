# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-07 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190906_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='house_number',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=150),
        ),
    ]
