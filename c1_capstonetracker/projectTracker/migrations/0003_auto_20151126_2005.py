# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0002_administrator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='contact_phone',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
