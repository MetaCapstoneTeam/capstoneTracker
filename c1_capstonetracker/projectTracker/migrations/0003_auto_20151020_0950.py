# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0002_auto_20151020_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='personal_picture',
            field=models.ImageField(upload_to='', null=True, blank=True),
        ),
    ]
