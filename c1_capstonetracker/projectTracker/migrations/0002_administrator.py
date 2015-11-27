# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('baseuser_ptr', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False, auto_created=True, parent_link=True)),
                ('position', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'administrator',
            },
            bases=('projectTracker.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
