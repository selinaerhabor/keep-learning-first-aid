# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-21 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningforkids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kidsquestion',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
