# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-01 00:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learningforkids', '0002_kidsquestion_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kidsquestion',
        ),
    ]