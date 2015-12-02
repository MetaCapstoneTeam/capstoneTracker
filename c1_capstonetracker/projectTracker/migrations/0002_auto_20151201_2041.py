# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='extra_info',
            field=models.FileField(null=True, blank=True, upload_to='updates'),
        ),
    ]
