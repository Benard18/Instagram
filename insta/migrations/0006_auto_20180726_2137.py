# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20180726_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilepicture',
            field=models.ImageField(blank=True, default='images/jVr43h8.png', upload_to='images/'),
        ),
    ]