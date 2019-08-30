# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-29 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(choices=[('REVEREND', 'Reverend'), ('SIR', 'Sir'), ('DAME', 'Dame'), ('MR', 'Mr'), ('MRS', 'Mrs'), ('MS', 'Ms'), ('MISS', 'Miss')], max_length=50),
        ),
    ]
