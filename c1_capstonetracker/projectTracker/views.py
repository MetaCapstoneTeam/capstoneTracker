from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import EmployeeForm, SchoolForm
from .models import Employee, Project, School, Student


def home_page(request):
    """Show the home page."""
    return render(request, 'home_page.html')


def project_list(request):
    """Show the list of Projects."""
    context = {}
    context['projects'] = Project.objects.all()
    return render(request, 'project_list.html', context)


def project_details(request, project_id):
    """Show the details of a project."""
    context = {}
    project = Project.objects.get(id=project_id)
    context['project'] = project
    return render(request, 'project_details.html', context)


def school_list(request):
    """Show the list of Schools."""
    context = {}
    context['schools'] = School.objects.all()
    return render(request, 'school_list.html', context)


def student_list(request):
    """Show the list of Students."""
    context = {}
    context['students'] = Student.objects.all()
    return render(request, 'student_list.html', context)


def employee_list(request):
    """Show the list of employees."""
    context = {}
    context['employees'] = Employee.objects.all()
    return render(request, 'employee_list.html', context)


def add_school(request):
    """Add school."""
    context = {}
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home_page.html', context)
        else:
            context['form'] = form
    else:
        context['form'] = SchoolForm()
    return render(request, 'add_school.html', context)


def add_employee(request):
    """Add employee."""
    context = {}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_profile.html', context)
        else:
            context['form'] = form
    else:
        context['form'] = EmployeeForm()
    return render(request, 'add_employee.html', context)


def login_user(request):
    """Check the credential of the user logging in."""
    username = password = ''
    state = "Log In"
    context = {}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = ""
            else:
                state = "Your account is not active, contact the admin. "
        else:
            state = "Your username and/or password were incorrect."

    context["state"] = state
    context["username"] = username
    if state == "":
        return redirect('home_page')
    else:
        return render(request, 'index.html', context)


def user_profile(request):
    """Show the profile of a user."""
    context = {}
    user = User.objects.all()
    context['users'] = user
    return render(request, 'user_profile.html', context)
