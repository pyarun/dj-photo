# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='path',
        ),
        migrations.AddField(
            model_name='photo',
            name='file',
            field=models.FileField(default='defauult', upload_to=b''),
            preserve_default=False,
        ),
    ]