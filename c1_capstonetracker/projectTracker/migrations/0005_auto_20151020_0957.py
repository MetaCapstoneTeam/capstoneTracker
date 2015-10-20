# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0004_auto_20151020_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='school_teams',
        ),
        migrations.RemoveField(
            model_name='schoolteam',
            name='mentors',
        ),
    ]
