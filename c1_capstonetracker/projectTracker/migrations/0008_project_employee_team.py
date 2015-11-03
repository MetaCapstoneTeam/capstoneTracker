# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0007_remove_project_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='employee_team',
            field=models.ForeignKey(to='projectTracker.Employee', null=True),
        ),
    ]
