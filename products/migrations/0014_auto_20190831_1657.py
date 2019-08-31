# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-31 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20190830_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Courses', 'Courses'), ('First Aid Kits', 'First Aid Kits'), ('Books', 'Books'), ('E-Books', 'E-Books'), ('CDs & DVDs', 'CDs & DVDs'), ('Manikins', 'Manikins'), ('Posters', 'Posters'), ('Extras', 'Extras')], default='', max_length=250),
        ),
    ]
