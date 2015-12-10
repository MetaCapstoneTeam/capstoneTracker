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


"""class EditStudentForm(ModelForm):

    Edit Student Form class.

    def __init__(self, **kwargs):
        self.first_name = kwargs.pop('first_name', None)
        self.last_name = kwargs.pop('last_name', None)
        super(EditStudentForm, self).__init__(**kwargs)

    def save(self, commit=True):
        obj = super(EditStudentForm, self).save(commit=False)
        obj.first_name = self.first_name
        obj.last_name = self.last_name
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email',
                  'phone', 'personal_picture', 'grad_semester',
                  'grad_year', 'major', 'school', 'username',
                  'password']

"""
class EmployeeForm(ModelForm):

    """Employee Form class."""

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'position', 'personal_picture', 'username', 'password']


class AdministratorForm(ModelForm):

    """Administrator Form class."""

    class Meta:
        model = Administrator
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


class UpdateForm(ModelForm):

    """Update Form clss."""

    class Meta:
        model = Update
        fields = ['subject', 'message', 'extra_info']
