# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-16 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0018_remove_vote_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='extra',
            field=models.TextField(null=True),
        ),
    ]