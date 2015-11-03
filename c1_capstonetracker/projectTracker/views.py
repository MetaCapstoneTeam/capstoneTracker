from django.shortcuts import render

from .models import Project, Student


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


def student_list(request):
    """Show the list of Students."""
    context = {}
    context['students'] = Student.objects.all()
    return render(request, 'student_list.html', context)
