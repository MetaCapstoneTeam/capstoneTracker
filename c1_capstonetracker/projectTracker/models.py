from django.contrib.auth.models import AbstractUser
from django.db import models


class Project(models.Model):

    """Project - Information about a capstone Project."""

    name = models.CharField(max_length=255, null=True)
    proposal = models.TextField()


class SchoolTeam(models.Model):

    """SchoolTeam-- Information about a School team."""

    student_members = models.ManyToManyField('Student')
    employee_members = models.ManyToManyField('Employee')
    school = models.ForeignKey('School')
    project = models.ForeignKey('Project')
    semester = models.CharField(max_length=255, blank=True)
    year = models.PositiveIntegerField()


class School(models.Model):

    """School - Information about a School."""

    name = models.CharField(max_length=255, null=True)
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=10, blank=True)


class BaseUser(AbstractUser):

    """Base User - Information about a User."""

    phone = models.CharField(max_length=10, blank=True)
    school_team = models.ForeignKey('SchoolTeam', null=True)


class Student(BaseUser):

    """Student - Information about a Student."""

    personal_picture = models.ImageField(
        upload_to='../media/personal_pictures', blank=True, null=True)
    grad_semester = models.CharField(max_length=255, blank=True)
    grad_year = models.PositiveIntegerField(blank=True)
    major = models.CharField(max_length=255, blank=True)
    school = models.ForeignKey('School')

    class Meta:
        verbose_name = 'student'


class Employee(BaseUser):

    """Employee - Information about a Employee."""

    position = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'employee'


class Administrator(BaseUser):

    """Administrator - Information about Admin Users."""

    position = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'administrator'


class Update(models.Model):

    """Update - the submission of group updates about their projects."""

    subject = models.CharField(max_length=255)
    message = models.TextField()
    extra_info = models.FileField(upload_to='../project/updates')
    project = models.ForeignKey('project')
