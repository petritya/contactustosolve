# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactustosolve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerEmail',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='Ügyfél e-mail címe'),
        ),
    ]
