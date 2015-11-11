from django.db import models


class Project(models.Model):

    """Project - Information about a capstone Project."""

    name = models.CharField(max_length=255, null=True)
    team = models.ManyToManyField('Employee')
    proposal = models.TextField()


class SchoolTeam(models.Model):

    """SchoolTeam-- Information about a School team."""

    team_members = models.ManyToManyField('Student')
    project_id = models.ForeignKey('Project')
    school_id = models.ForeignKey('School')
    semester = models.CharField(max_length=255, blank=True)


class School(models.Model):

    """School - Information about a School."""

    name = models.CharField(max_length=255, null=True)
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=10)


class Student(models.Model):

    """Student - Information about a Student."""

    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True)
    personal_picture = models.ImageField(null=True, blank=True)
    grad_semester = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=255, blank=True)
    school = models.ForeignKey('School')


class Employee(models.Model):

    """Employee - Information about a Employee."""
    
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True)
    position = models.CharField(max_length=255, blank=True)

   # @classmethod
   # def create():
