from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class ProjectForm(ModelForm):

    """Project Form class."""

    class Meta:
        model = Project
        fields = ['name', 'team', 'proposal']


class StudentForm(ModelForm):

    """Student Form class."""

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email',
                  'phone', 'personal_picture', 'grad_semester',
                  'major', 'school']


class EmployeeForm(ModelForm):

    """Employee Form class."""

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'position']

class UserForm(ModelForm):

    """User Form class."""

    class Meta:
        model = User
        fields = ['username', 'password' ]


class SchoolForm(ModelForm):

    """School Form class."""

    class Meta:
        model = School
        fields = ['name', 'contact_first_name', 'contact_last_name',
                  'contact_email', 'contact_phone']


class SchoolTeam(ModelForm):

    """School Team Form class."""

    class Meta:
        model = SchoolTeam
        fields = ['team_members', 'project_id', 'school_id', 'semester']
