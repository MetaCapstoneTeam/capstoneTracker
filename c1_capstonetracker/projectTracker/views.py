from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import AdministratorForm, EmployeeForm, ProjectForm, SchoolForm
from .forms import SchoolTeamForm, StudentForm, UpdateForm

from .models import Administrator, BaseUser, Employee, Project, School
from .models import SchoolTeam, Student, Update

from .groups import *

def home_page(request):
    """Show the home page."""
    if request.user.is_authenticated():
        context = {}
        context['user'] = request.user
        return render(request, 'home_page.html', context)

    else:
        return redirect('/')


def project_list(request):
    """Show the list of Projects."""
    if request.user.is_authenticated():
        context = {}
        context['projects'] = Project.objects.all()
        return render(request, 'project_list.html', context)
    else:
        return redirect('/')


def school_list(request):
    """Show the list of Schools."""
    if request.user.is_authenticated():
        context = {}
        context['schools'] = School.objects.all()
        return render(request, 'school_list.html', context)
    else:
        redirect('/')


def student_list(request):
    """Show the list of Students."""
    if request.user.is_authenticated():
        context = {}
        context['students'] = Student.objects.all().order_by('last_name')
        return render(request, 'student_list.html', context)
    else:
        redirect('/')


def employee_list(request):
    """Show the list of employees."""
    if request.user.is_authenticated():
        context = {}
        context['employees'] = Employee.objects.all()
        return render(request, 'employee_list.html', context)
    else:
        redirect('/')


def team_list(request):
    """Show the list of teams."""
    if request.user.is_authenticated():
        context = {}
        context['teams'] = SchoolTeam.objects.all()
        return render(request, 'team_list.html', context)
    else:
        redirect('/')


def admin_list(request):
    """Show the list of teams."""
    if request.user.is_authenticated():
        context = {}
        context['admins'] = Administrator.objects.all()
        return render(request, 'admin_list.html', context)
    else:
        redirect('/')


def add_school(request):
    """Add school."""
    if request.user.is_authenticated():
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
    else:
        redirect('/')


def add_employee(request):
    """Add employee."""
    if request.user.is_authenticated():
        context = {}
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                BaseUser.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    phone=request.POST['phone'])
                auth_user = authenticate(
                    username=request.POST['username'],
                    password=request.POST['password'])
                employee = Employee(baseuser_ptr_id=auth_user.id,
                                    position=request.POST['position'])
                employee.__dict__.update(auth_user.__dict__)
                employee.groups.add(employee_users())
                employee.save()
                return redirect('/projectTracker/employeelist/')
            else:
                context['form'] = form
        else:
            context['form'] = EmployeeForm()
        return render(request, 'add_employee.html', context)
    else:
        redirect('/')


def add_student(request):
    """Add student."""
    if request.user.is_authenticated():
        context = {}
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES)
            if form.is_valid():
                BaseUser.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    phone=request.POST['phone'])
                auth_user = authenticate(
                    username=request.POST['username'],
                    password=request.POST['password'])
                student = Student(
                    baseuser_ptr_id=auth_user.id,
                    grad_semester=request.POST['grad_semester'],
                    grad_year=request.POST['grad_year'],
                    major=request.POST['major'],
                    school=School.objects.get(id=request.POST['school']),
                    personal_picture=request.FILES.get('personal_picture',None))
                student.__dict__.update(auth_user.__dict__)
                student.groups.add(student_users())
                student.save()
                return redirect('/projectTracker/studentlist/')
            else:
                context['form'] = form
        else:
            context['form'] = StudentForm()
        return render(request, 'add_student.html', context)
    else:
        redirect('/')


def add_admin(request):
    """Add Administrator."""
    if request.user.is_authenticated():
        context = {}
        if request.method == 'POST':
            form = AdministratorForm(request.POST)
            if form.is_valid():
                BaseUser.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    phone=request.POST['phone'])
                auth_user = authenticate(
                    username=request.POST['username'],
                    password=request.POST['password'])
                admin = Administrator(baseuser_ptr_id=auth_user.id,
                                      position=request.POST['position'])
                admin.__dict__.update(auth_user.__dict__)
                admin.groups.add(administrative_users())
                admin.save()
                return redirect('/projectTracker/administratorlist/')
            else:
                context['form'] = form
        else:
            context['form'] = AdministratorForm()
        context['admins'] = Administrator.objects.all()
        return render(request, 'add_admin.html', context)
    else:
        redirect('/')


def add_project(request):
    """Add project."""
    if request.user.is_authenticated():
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
    else:
        redirect('/')


def add_team(request):
    """Add team."""
    if request.user.is_authenticated():
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
    else:
        redirect('/')


def add_update(request, team_id):
    """Add update."""
    if request.user.is_authenticated():
        context = {}
        if request.method == 'POST':
            form = UpdateForm(request.POST, request.FILES)
            if form.is_valid():
                update = Update(
                    subject=request.POST['subject'],
                    message=request.POST['message'],
                    extra_info=request.FILES.get('extra_info', None),
                    team=SchoolTeam.objects.get(id=team_id))
                update.save()
                return redirect('my_project')
            else:
                context['form'] = form
        else:
            context['form'] = UpdateForm()
        return render(request, 'add_update.html', context)
    else:
        redirect('/')


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
    """log the user out."""
    logout(request)
    return render(request, 'index.html')


def user_profile(request, user_id):
    """Show the profile of a user."""
    if request.user.is_authenticated():
        context = {}
        user = BaseUser.objects.get(id=user_id)
        context['user'] = user
        context['is_student'] = user.has_perm('projectTracker.has_student_profile')
        context['is_employee'] = user.has_perm('projectTracker.has_employee_profile')
        return render(request, 'user_profile.html', context)
    else:
        redirect('/')


def my_project(request):
    """Show the project of current user, allow updates."""
    if request.user.is_authenticated():
        context = {}

        if SchoolTeam.objects.filter(student_members=request.user):
            teams = list(SchoolTeam.objects.filter(
                student_members=request.user))
        else:
            teams = list(SchoolTeam.objects.filter(
                employee_members=request.user))
        for team in range(len(teams)):
            teams[team].updates = list(Update.objects.filter(team=teams[team]).order_by('-timestamp'))
            print("hi")
            print(teams[team].updates)
        context['teams'] = teams
        
        return render(request, 'my_project.html', context)
    else:
        redirect('/')
