# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0020_auto_20171003_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='contents/'),
        ),
    ]