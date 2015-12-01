# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0006_auto_20151129_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='personal_picture',
            field=models.ImageField(null=True, upload_to='personal_pictures', blank=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='extra_info',
            field=models.FileField(upload_to='updates'),
        ),
    ]
