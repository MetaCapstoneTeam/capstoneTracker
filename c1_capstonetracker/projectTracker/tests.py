# from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .models import Administrator, Employee, Project, School, SchoolTeam
from .models import Student
from .views import admin_list, employee_list, project_list, school_list
from .views import student_list, team_list


class ProjectTrackerViewsTests(TestCase):

    """Test the project tracker views."""

    def setUp(self):
        """set up test data."""
        self.test_project = Project.objects.create(name='Test Project')
        self.test_school = School.objects.create(name='Test School',
                                                 contact_first_name='John',
                                                 contact_last_name='Smith',
                                                 contact_email='t@email.com')
        self.test_student = Student.objects.create(username='testStudent',
                                                   email='test@email.com',
                                                   password='pass',
                                                   school=self.test_school,
                                                   grad_year=2015)
        self.test_employee = Employee.objects.create(username='testEmployee',
                                                     email='test@email.com',
                                                     password='pass')
        self.test_admin = Administrator.objects.create(username='testAdmin',
                                                       email='test@email.com',
                                                       password='pass')

    def test_project_list_view_returns_correct_html(self):
        """Test that the project list view returns correct html."""
        request = HttpRequest()
        request.user = self.test_employee
        response = project_list(request)
        context = {}
        context['projects'] = Project.objects.all()
        context['user'] = self.test_employee
        expected_content = render_to_string('project_list.html', context)
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )

    def test_school_list_view_returns_correct_html(self):
        """Test that the school list view returns correct html."""
        request = HttpRequest()
        request.user = self.test_student
        response = school_list(request)
        context = {}
        context['schools'] = School.objects.all()
        context['user'] = self.test_student
        expected_content = render_to_string('school_list.html', context)
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )

    def test_student_list_view_returns_correct_html(self):
        """Test that the student list view returns correct html."""
        request = HttpRequest()
        request.user = self.test_student
        response = student_list(request)
        context = {}
        context['students'] = Student.objects.all()
        context['user'] = self.test_student
        expected_content = render_to_string('student_list.html', context)
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )

    def test_employee_list_view_returns_correct_html(self):
        """Test that the employee list view returns correct html."""
        request = HttpRequest()
        request.user = self.test_employee
        response = employee_list(request)
        context = {}
        context['employees'] = Employee.objects.all()
        context['user'] = self.test_employee
        expected_content = render_to_string('employee_list.html', context)
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )

    def test_team_list_view_returns_correct_html(self):
        """Test that the team list view returns the correct html."""
        request = HttpRequest()
        request.user = self.test_employee
        response = team_list(request)
        context = {}
        context['teams'] = SchoolTeam.objects.all()
        context['user'] = self.test_employee
        expected_content = render_to_string('team_list.html', context)
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )

    def test_admin_list_view_returns_correct_html(self):
        """Test that the team list view returns the correct html."""
        request = HttpRequest()
        request.user = self.test_admin
        response = admin_list(request)
        context = {}
        context['admins'] = Administrator.objects.all()
        context['user'] = self.test_admin
        expected_content = render_to_string('admin_list.html', context)
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )
