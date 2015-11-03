# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0008_project_employee_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employee_team',
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(to='projectTracker.Employee'),
        ),
    ]
