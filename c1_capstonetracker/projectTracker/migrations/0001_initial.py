# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=255)),
                ('proposal', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=255)),
                ('contact_first_name', models.CharField(max_length=255)),
                ('contact_last_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('semester', models.CharField(max_length=255, blank=True)),
                ('year', models.PositiveIntegerField()),
                ('project_id', models.ForeignKey(to='projectTracker.Project')),
                ('school_id', models.ForeignKey(to='projectTracker.School')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('baseuser_ptr', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False, auto_created=True, parent_link=True)),
                ('position', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'employee',
            },
            bases=('projectTracker.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('baseuser_ptr', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False, auto_created=True, parent_link=True)),
                ('personal_picture', models.ImageField(null=True, upload_to='', blank=True)),
                ('grad_semester', models.CharField(max_length=255, blank=True)),
                ('major', models.CharField(max_length=255, blank=True)),
                ('school', models.ForeignKey(to='projectTracker.School')),
            ],
            options={
                'verbose_name': 'student',
            },
            bases=('projectTracker.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(to='projectTracker.SchoolTeam'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_name='user_set'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', blank=True, related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions', related_name='user_set'),
        ),
        migrations.AddField(
            model_name='schoolteam',
            name='employee_members',
            field=models.ManyToManyField(to='projectTracker.Employee'),
        ),
        migrations.AddField(
            model_name='schoolteam',
            name='student_members',
            field=models.ManyToManyField(to='projectTracker.Student'),
        ),
    ]
