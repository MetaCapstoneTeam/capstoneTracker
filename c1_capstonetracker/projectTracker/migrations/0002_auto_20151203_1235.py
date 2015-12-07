# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grad_semester',
            field=models.CharField(choices=[('FA', 'Fall'), ('SP', 'Spring'), ('SU', 'Summer')], max_length=2),
        ),
    ]
