# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tip',
            options={'permissions': (('downvote_tip', 'Can downvote a tip.'),)},
        ),
    ]
