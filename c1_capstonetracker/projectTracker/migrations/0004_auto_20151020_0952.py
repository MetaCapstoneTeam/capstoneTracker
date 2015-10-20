# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0003_auto_20151020_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolteam',
            name='team_members',
        ),
        migrations.AddField(
            model_name='schoolteam',
            name='team_members',
            field=models.ManyToManyField(to='projectTracker.Student'),
        ),
    ]
