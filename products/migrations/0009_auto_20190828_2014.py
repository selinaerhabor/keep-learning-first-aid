# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-28 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190828_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured',
        ),
        migrations.AddField(
            model_name='product',
            name='featured_page',
            field=models.CharField(choices=[('N', 'No'), ('H', 'Home'), ('LFK', 'Learning For Kids'), ('LFA', 'Learning For Adults')], default='', max_length=1),
        ),
    ]
