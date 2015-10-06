from django.db import models


class Project(models.Model):

    """Project - Information about the capstone Project"""

    school_teams = models.ForeignKey('SchoolTeam')
    project_team = models.ManyToManyField('Employee')
    proposal = models.TextField()

class SchoolTeam(models.Model):
    """SchoolTeam-- Information about the School team"""

    mentors = models.ManyToManyField('Employee')
    team_members = models.ForeignKey('Student')
    project_id = models.ForeignKey('Project')
    school_id = models.ForeignKey('School')
    semester = models.CharField(max_length=255, blank=True)

class School(models.Model):
    name = models.CharField(max_length=255)
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=10)

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    personal_picture = models.ImageField()
    grad_semester = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    school = models.ForeignKey('School')

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    position = models.CharField(max_length=255)