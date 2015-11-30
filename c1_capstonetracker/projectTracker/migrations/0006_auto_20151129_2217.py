# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectTracker', '0005_baseuser_school_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('extra_info', models.FileField(upload_to='../project/updates')),
                ('project', models.ForeignKey(to='projectTracker.Project')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_picture',
            field=models.ImageField(blank=True, null=True, upload_to='../media/personal_pictures'),
        ),
    ]
