from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render


from .forms import EmployeeForm, SchoolForm, UserForm
from .models import Employee, Project, School, Student

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
        userform = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
            new_user.first_name = request.POST['first_name']
            new_user.last_name = request.POST['last_name']
            new_user.save()
            form.save()
            return render(request, 'home_page.html', context)
        else:
            context['form'] = form
            context['userForm'] = userform
    else:
        context['form'] = EmployeeForm()
        context['userForm'] = UserForm()
    return render(request, 'add_employee.html', context)


def login_user(request):
    """Check the credential of the user logging in."""
    username = password = ''
    state = ""
    context = {}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_type = request.POST.get('login_t')
        print(login_type)
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
