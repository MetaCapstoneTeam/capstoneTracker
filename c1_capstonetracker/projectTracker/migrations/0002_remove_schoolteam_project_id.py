# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolteam',
            name='project_id',
        ),
    ]
