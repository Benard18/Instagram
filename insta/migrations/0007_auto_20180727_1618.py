# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_auto_20180726_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilepicture',
            field=models.ImageField(blank=True, default='/jVr43h8.png', upload_to='images/'),
        ),
    ]