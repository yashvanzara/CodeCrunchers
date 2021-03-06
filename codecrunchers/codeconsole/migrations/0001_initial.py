# -*- coding: utf-8 -*-
# <<<<<<< HEAD
# # Generated by Django 1.10.4 on 2017-03-30 04:21
# =======
# # Generated by Django 1.10.4 on 2017-03-30 04:12
# >>>>>>> 23e143b810f01ad69a92b3141a0cfca946c3e6e4
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsoleLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_code', models.CharField(max_length=255, unique=True, verbose_name='Code')),
                ('lang', models.CharField(max_length=255, unique=True, verbose_name='Language')),
                ('ace_file_name', models.CharField(max_length=255, verbose_name='Editor filename')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
            ],
        ),
    ]
