# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0006_auto_20151020_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
    ]
