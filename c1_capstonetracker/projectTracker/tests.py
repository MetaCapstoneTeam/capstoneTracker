# from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .models import Employee, Project, School, Student
from .views import employee_list, home_page, project_details
from .views import project_list, school_list, student_list


class ProjectTrackerViewsTests(TestCase):

    """Test the project tracker views."""

    def setUp(self):
        """set up test data."""
        self.test_project = Project.objects.create(name='Test Project')
        self.test_school = School.objects.create(name='Test School',
                                                 contact_first_name='John',
                                                 contact_last_name='Smith',
                                                 contact_email='tt@email.com')
        self.test_student = Student.objects.create(username='testStudent',
                                                   email='t@email.com',
                                                   password='pass',
                                                   school=self.test_school)
        self.test_employee = Employee.objects.create(username='testEmployee',
                                                     email='ttt@email.com',
                                                     password='pass')

    def test_home_page_view_returns_correct_html(self):
        """Test that the home page view returns correct html."""
        request = HttpRequest()
        request.user = self.test_student
        response = home_page(request)
        expected_content = render_to_string('home_page.html')
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )

    def test_project_details_view_returns_correct_html(self):
        """Test that the project details view returns correct html."""
        request = HttpRequest()
        request.user = self.test_student
        response = project_details(request, self.test_project.id)
        context = {}
        project = Project.objects.get(id=self.test_project.id)
        context['project'] = project
        expected_content = render_to_string('project_details.html', context)
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )

    def test_project_list_view_returns_correct_html(self):
        """Test that the project list view returns correct html."""
        request = HttpRequest()
        request.user = self.test_employee
        response = project_list(request)
        context = {}
        context['projects'] = Project.objects.all()
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
        expected_content = render_to_string('employee_list.html', context)
        self.assertEqual(
            response.content.decode('utf8'),
            expected_content
        )
