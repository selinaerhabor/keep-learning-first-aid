# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-06 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190829_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_line1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line2',
            new_name='address_line_2',
        ),
    ]
