from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render

from .forms import EmployeeForm, ProjectForm, SchoolForm, SchoolTeamForm, StudentForm
from .models import BaseUser, Employee, Project, School, SchoolTeam, Student


#emp_content_type = ContentType.objects.get(app_label='projectTracker', model='Employee')
#Permission.objects.create(codename='can_see_lists',
                                      # name='Can See Lists of Students, Employees, Projects, and Schools',
                                      # content_type=emp_content_type)

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

def team_list(request):
    """Show the list of teams."""
    context = {}
    context['teams'] = SchoolTeam.objects.all()
    return render(request, 'team_list.html', context)


def add_school(request):
    """Add school."""
    context = {}
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projectTracker/schoollist/')
        else:
            context['form'] = form
    else:
        context['form'] = SchoolForm()
    context['schools'] = School.objects.all()
    return render(request, 'add_school.html', context)


def add_employee(request):
    """Add employee."""
    context = {}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            BaseUser.objects.create_user(username=request.POST['username'],
                                         password=request.POST['password'],
                                         first_name=request.POST['first_name'],
                                         last_name=request.POST['last_name'],
                                         email=request.POST['email'],
                                         phone=request.POST['phone'])
            auth_user = authenticate(username=request.POST['username'],password=request.POST['password'])
            login(request,auth_user)
            employee = Employee(baseuser_ptr_id=auth_user.id,
                            position=request.POST['position'],)
            employee.__dict__.update(auth_user.__dict__)
            employee.save()
            return redirect('/projectTracker/employeelist/')
        else:
            context['form'] = form
    else:
        context['form'] = EmployeeForm()
    return render(request, 'add_employee.html', context)

def add_student(request):
    """Add student."""
    context = {}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            BaseUser.objects.create_user(username=request.POST['username'],
                                         password=request.POST['password'],
                                         first_name=request.POST['first_name'],
                                         last_name=request.POST['last_name'],
                                         email=request.POST['email'],
                                         phone=request.POST['phone'])
            auth_user = authenticate(username=request.POST['username'],password=request.POST['password'])
            login(request,auth_user)
            student = Student(baseuser_ptr_id=auth_user.id,
                            #personal_picture=request.POST['personal_picture'],
                            grad_semester=request.POST['grad_semester'],
                            major= request.POST['major'],
                            school=School.objects.get(id=request.POST['school']))
            student.__dict__.update(auth_user.__dict__)
            student.save()
            return redirect('/projectTracker/studentlist/')
        else:
            context['form'] = form
    else:
        context['form'] = StudentForm()
    return render(request, 'add_student.html', context)

def add_project(request):
    """Add project."""
    context = {}
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projectTracker/projectlist/')
        else:
            context['form'] = form
    else:
        context['form'] = ProjectForm()

    context['projects'] = Project.objects.all()
    return render(request, 'add_project.html', context)


def add_team(request):
    """Add team."""
    context = {}
    if request.method == 'POST':
        form = SchoolTeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projectTracker/teamlist/')
        else:
            context['form'] = form
    else:
        context['form'] = SchoolTeamForm()
    context['teams'] = SchoolTeam.objects.all()
    return render(request, 'add_team.html', context)


def login_user(request):
    """Check the credential of the user logging in."""
    username = password = ''
    state = ""
    context = {}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home_page')
            else:
                state = "Your account is not active, contact the admin. "
        else:
            state = "Your username and/or password were incorrect."
        context['state'] = state
        return render(request, 'index.html', context)


def logout_user(request):
    logout(request)
    return render(request,'index.html')

def user_profile(request):
    """Show the profile of a user."""
    context = {}
    user = request.user
    context['user'] = user
    # if  Employee.objects.get(email=user.email) != doesnotexists:
        # context['user'] = empl
    
    return render(request, 'user_profile.html', context)
