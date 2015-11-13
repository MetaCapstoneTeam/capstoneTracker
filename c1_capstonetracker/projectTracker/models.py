from django.contrib.auth.models import AbstractUser
from django.db import models


class Project(models.Model):

    """Project - Information about a capstone Project."""

    name = models.CharField(max_length=255, null=True)
    team = models.ForeignKey('SchoolTeam')
    proposal = models.TextField()


class SchoolTeam(models.Model):

    """SchoolTeam-- Information about a School team."""

    student_members = models.ManyToManyField('Student')
    employee_members = models.ManyToManyField('Employee')
    school_id = models.ForeignKey('School')
    semester = models.CharField(max_length=255, blank=True)
    year = models.PositiveIntegerField()


class School(models.Model):

    """School - Information about a School."""

    name = models.CharField(max_length=255, null=True)
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=10)


class BaseUser(AbstractUser):

    """Base User - Information about a User"""

    phone = models.CharField(max_length=10, blank=True)


class Student(BaseUser):

    """Student - Information about a Student."""

    personal_picture = models.ImageField(null=True, blank=True)
    grad_semester = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=255, blank=True)
    school = models.ForeignKey('School')

    class Meta:
        verbose_name = 'student'


class Employee(BaseUser):

    """Employee - Information about a Employee."""
    
    position = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'employee'
        

