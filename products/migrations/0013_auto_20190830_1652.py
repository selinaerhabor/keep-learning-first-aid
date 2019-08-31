# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-30 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20190830_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured_page',
            field=models.CharField(choices=[('N', 'No'), ('H', 'Home'), ('LFK', 'Learning For Kids'), ('LFA', 'Learning For Adults')], default='N', max_length=3),
        ),
    ]
