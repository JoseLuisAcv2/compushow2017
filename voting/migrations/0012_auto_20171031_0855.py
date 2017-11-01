# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-31 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0011_auto_20171030_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominee',
            name='entityOpt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entityOpt', to='voting.Entity'),
        ),
        migrations.AlterField(
            model_name='nominee',
            name='entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entity', to='voting.Entity'),
        ),
    ]