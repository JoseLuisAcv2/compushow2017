# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 02:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomination', '0011_auto_20170406_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominate',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nomination.Category'),
        ),
        migrations.AddField(
            model_name='nominate',
            name='nominee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nomination.Entity'),
        ),
        migrations.AlterField(
            model_name='nominate',
            name='nominator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]