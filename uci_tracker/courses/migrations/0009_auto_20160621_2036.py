# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20160621_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='wait_list',
            field=models.PositiveSmallIntegerField(),
        ),
    ]