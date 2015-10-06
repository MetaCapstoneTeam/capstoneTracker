# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('position', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('proposal', models.TextField()),
                ('project_team', models.ManyToManyField(to='projectTracker.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('contact_first_name', models.CharField(max_length=255)),
                ('contact_last_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('semester', models.CharField(max_length=255, blank=True)),
                ('mentors', models.ManyToManyField(to='projectTracker.Employee')),
                ('project_id', models.ForeignKey(to='projectTracker.Project')),
                ('school_id', models.ForeignKey(to='projectTracker.School')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('personal_picture', models.ImageField(upload_to='')),
                ('grad_semester', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('school', models.ForeignKey(to='projectTracker.School')),
            ],
        ),
        migrations.AddField(
            model_name='schoolteam',
            name='team_members',
            field=models.ForeignKey(to='projectTracker.Student'),
        ),
        migrations.AddField(
            model_name='project',
            name='school_teams',
            field=models.ForeignKey(to='projectTracker.SchoolTeam'),
        ),
    ]
