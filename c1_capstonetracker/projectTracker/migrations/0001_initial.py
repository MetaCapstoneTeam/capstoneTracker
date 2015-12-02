# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True)),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('proposal', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('contact_first_name', models.CharField(max_length=255)),
                ('contact_last_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=10, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=255, blank=True)),
                ('year', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='projectTracker.Project')),
                ('school', models.ForeignKey(to='projectTracker.School')),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('extra_info', models.FileField(upload_to='updates')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(to='projectTracker.SchoolTeam')),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('baseuser_ptr', models.OneToOneField(primary_key=True, auto_created=True, to=settings.AUTH_USER_MODEL, serialize=False, parent_link=True)),
                ('position', models.CharField(max_length=255, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'administrator',
            },
            bases=('projectTracker.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('baseuser_ptr', models.OneToOneField(primary_key=True, auto_created=True, to=settings.AUTH_USER_MODEL, serialize=False, parent_link=True)),
                ('position', models.CharField(max_length=255, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
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
                ('baseuser_ptr', models.OneToOneField(primary_key=True, auto_created=True, to=settings.AUTH_USER_MODEL, serialize=False, parent_link=True)),
                ('personal_picture', models.ImageField(upload_to='personal_pictures', blank=True, null=True)),
                ('grad_semester', models.CharField(max_length=255, blank=True)),
                ('grad_year', models.PositiveIntegerField(blank=True)),
                ('major', models.CharField(max_length=255, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
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
            model_name='baseuser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', to='auth.Group', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_name='user_set'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='school_team',
            field=models.ForeignKey(to='projectTracker.SchoolTeam', null=True),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', to='auth.Permission', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_name='user_set'),
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
