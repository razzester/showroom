# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Qualification',
            field=models.TextField(max_length=50),
        ),
    ]
