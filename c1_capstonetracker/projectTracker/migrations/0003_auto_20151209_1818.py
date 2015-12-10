# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0002_auto_20151203_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolteam',
            name='semester',
            field=models.CharField(choices=[('FA', 'Fall'), ('SP', 'Spring'), ('SU', 'Summer')], max_length=2),
        ),
    ]
