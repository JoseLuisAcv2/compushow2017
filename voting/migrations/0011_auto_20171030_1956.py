# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-30 23:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0010_auto_20170417_2153'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nominate',
            unique_together=set([]),
        ),
    ]
