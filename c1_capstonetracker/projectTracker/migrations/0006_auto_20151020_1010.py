# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0005_auto_20151020_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_team',
            new_name='team',
        ),
    ]
