# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0004_student_grad_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='school_team',
            field=models.ForeignKey(null=True, to='projectTracker.SchoolTeam'),
        ),
    ]
