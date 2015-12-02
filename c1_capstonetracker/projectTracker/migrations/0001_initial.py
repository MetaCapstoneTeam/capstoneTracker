# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', max_length=30, error_messages={'unique': 'A user with that username already exists.'}, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=10, blank=True)),
                ('bio', models.TextField(blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, max_length=255)),
                ('proposal', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, max_length=255)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('extra_info', models.FileField(upload_to='updates', null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(to='projectTracker.SchoolTeam')),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
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
                ('baseuser_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
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
                ('baseuser_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('personal_picture', models.ImageField(upload_to='personal_pictures', default='image-not-available.jpeg', blank=True)),
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
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_query_name='user', related_name='user_set', blank=True, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', verbose_name='user permissions', related_query_name='user', related_name='user_set', blank=True, to='auth.Permission'),
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
