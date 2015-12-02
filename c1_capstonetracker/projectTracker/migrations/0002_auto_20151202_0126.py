# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='personal_picture',
            field=models.ImageField(upload_to='personal_pictures', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_picture',
            field=models.ImageField(upload_to='personal_pictures', blank=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
