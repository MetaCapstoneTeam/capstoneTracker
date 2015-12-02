from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def administrative_users():
    return Group.objects.get(
        name='Administrative Users')

def employee_users():
    return Group.objects.get(
        name='Employee Users')

def student_users():
    return Group.objects.get(
        name='Student Users')

def can_view_students():
    return Permission.objects.get(
        name='Can View Students',
        codename='can_view_students',
        content_type=admin_ct)

def can_view_employees():
    return Permission.objects.get(
        name='Can View Employees',
        codename='can_view_employees',
        content_type=admin_ct)

def can_view_projects():
    return Permission.objects.get(
        name='Can View Projects',
        codename='can_view_projects',
        content_type=admin_ct)

def can_view_teams():
    return Permission.objects.get(
        name='Can View Teams',
        codename='can_view_teams',
        content_type=admin_ct)

def can_view_schools():
    return Permission.objects.get(
        name='Can View Schools',
        codename='can_view_schools',
        content_type=admin_ct)

def can_view_admins():
    return Permission.objects.get(
        name='Can View Administrators',
        codename='can_view_admins',
        content_type=admin_ct)


def can_edit_students():
    return Permission.objects.get(
        name='Can Edit Students ',
        codename='can_edit_students',
        content_type=admin_ct)

def can_edit_schools():
    return Permission.objects.get(
        name='Can Edit Schools ',
        codename='can_edit_schools',
        content_type=admin_ct)

def can_edit_employees():
    return Permission.objects.get(
        name='Can Edit Employees ',
        codename='can_edit_employees',
        content_type=admin_ct)

def can_edit_teams():
    return Permission.objects.get(
        name='Can Edit Teams ',
        codename='can_edit_teams',
        content_type=admin_ct)

def can_edit_projects ():
    return Permission.objects.get(
    name='Can Edit Projects ',
    codename='can_edit_projects',
    content_type=admin_ct)


def can_edit_admins():
    return Permission.objects.get(
        name='Can Edit Administrators ',
        codename='can_edit_admins',
        content_type=admin_ct)

def has_student_profile():
    return Permission.objects.get(
        name='Is A Student User',
        codename='has_student_profile',
        content_type=admin_ct)

def has_employee_profile():
    return Permission.objects.get(
        name='Is an Employee User',
        codename='has_employee_profile',
        content_type=admin_ct)

def has_project():
    return Permission.objects.get(
        name='Has a my Project Page',
        codename='has_project',
        content_type=admin_ct)


administrative_users.permissions = [can_view_teams, can_edit_teams,
                                    can_view_projects, can_edit_projects,
                                    can_view_employees, can_edit_employees,
                                    can_view_students, can_edit_students,
                                    can_view_schools, can_edit_schools,
                                    can_view_admins, can_edit_admins]

employee_users.permissions = [can_view_teams, can_view_projects,
                              can_view_employees, can_view_students,
                              can_view_schools, has_employee_profile,
                              has_project]

student_users.permissions = [has_student_profile, has_project]
