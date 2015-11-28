from django.forms import ModelForm

from .models import *


class ProjectForm(ModelForm):

    """Project Form class."""

    class Meta:
        model = Project
        fields = ['name', 'proposal']


class StudentForm(ModelForm):

    """Student Form class."""

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email',
                  'phone', 'personal_picture', 'grad_semester',
                  'grad_year', 'major', 'school', 'username',
                  'password']


class EmployeeForm(ModelForm):

    """Employee Form class."""

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'position', 'username', 'password']


class SchoolForm(ModelForm):

    """School Form class."""

    class Meta:
        model = School
        fields = ['name', 'contact_first_name', 'contact_last_name',
                  'contact_email', 'contact_phone']


class SchoolTeamForm(ModelForm):

    """School Team Form class."""

    class Meta:
        model = SchoolTeam
        fields = ['student_members', 'employee_members', 'school',
                  'project', 'semester', 'year']
