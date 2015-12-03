# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.contrib.auth.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(unique=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('phone', models.CharField(blank=True, max_length=10)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=255)),
                ('proposal', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=255)),
                ('contact_first_name', models.CharField(max_length=255)),
                ('contact_last_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(blank=True, max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('semester', models.CharField(blank=True, max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='projectTracker.Project')),
                ('school', models.ForeignKey(to='projectTracker.School')),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
                ('extra_info', models.FileField(blank=True, upload_to='updates', null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(to='projectTracker.SchoolTeam')),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('baseuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('position', models.CharField(blank=True, max_length=255)),
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
                ('baseuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('personal_picture', models.ImageField(upload_to='personal_pictures', blank=True)),
                ('position', models.CharField(blank=True, max_length=255)),
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
                ('baseuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('personal_picture', models.ImageField(upload_to='personal_pictures', blank=True)),
                ('grad_semester', models.CharField(blank=True, max_length=255)),
                ('grad_year', models.PositiveIntegerField(blank=True)),
                ('major', models.CharField(blank=True, max_length=255)),
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
            field=models.ManyToManyField(to='auth.Group', related_query_name='user', related_name='user_set', blank=True, verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', related_query_name='user', related_name='user_set', blank=True, verbose_name='user permissions', help_text='Specific permissions for this user.'),
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
