# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0017_program_contentsnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='contents/'),
        ),
    ]