from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def admin_ct():
    """declare admin_ct."""
    return ContentType.objects.get(app_label='projectTracker',
                                   model='Administrator')


def administrative_users():
    """Admin Group."""
    return Group.objects.get(
        name='Administrative Users')


def employee_users():
    """Employee Group."""
    return Group.objects.get(
        name='Employee Users')


def student_users():
    """Student Group."""
    return Group.objects.get(
        name='Student Users')


def can_view_students():
    """Can View Student Permission."""
    return Permission.objects.get(
        name='Can View Students',
        codename='can_view_students',
        content_type=admin_ct())


def can_view_employees():
    """Can View employee Permission."""
    return Permission.objects.get(
        name='Can View Employees',
        codename='can_view_employees',
        content_type=admin_ct())


def can_view_projects():
    """Can View project Permission."""
    return Permission.objects.get(
        name='Can View Projects',
        codename='can_view_projects',
        content_type=admin_ct())


def can_view_teams():
    """Can View Teams Permission."""
    return Permission.objects.get(
        name='Can View Teams',
        codename='can_view_teams',
        content_type=admin_ct())


def can_view_schools():
    """Can View Schools Permission."""
    return Permission.objects.get(
        name='Can View Schools',
        codename='can_view_schools',
        content_type=admin_ct())


def can_view_admins():
    """Can View Admin Permission."""
    return Permission.objects.get(
        name='Can View Administrators',
        codename='can_view_admins',
        content_type=admin_ct())


def can_edit_students():
    """Can Edit Student Permission."""
    return Permission.objects.get(
        name='Can Edit Students ',
        codename='can_edit_students',
        content_type=admin_ct())


def can_edit_schools():
    """Can Edit Schools Permission."""
    return Permission.objects.get(
        name='Can Edit Schools ',
        codename='can_edit_schools',
        content_type=admin_ct())


def can_edit_employees():
    """Can Edit employee Permission."""
    return Permission.objects.get(
        name='Can Edit Employees ',
        codename='can_edit_employees',
        content_type=admin_ct())


def can_edit_teams():
    """Can Edit Teams Permission."""
    return Permission.objects.get(
        name='Can Edit Teams ',
        codename='can_edit_teams',
        content_type=admin_ct())


def can_edit_projects():
    """Can Edit project Permission."""
    return Permission.objects.get(
        name='Can Edit Projects ',
        codename='can_edit_projects',
        content_type=admin_ct())


def can_edit_admins():
    """Can Edit Admin Permission."""
    return Permission.objects.get(
        name='Can Edit Administrators ',
        codename='can_edit_admins',
        content_type=admin_ct())


def has_student_profile():
    """student profile permissions."""
    return Permission.objects.get(
        name='Is A Student User',
        codename='has_student_profile',
        content_type=admin_ct())


def has_employee_profile():
    """employee profile permissions."""
    return Permission.objects.get(
        name='Is an Employee User',
        codename='has_employee_profile',
        content_type=admin_ct())


def has_project():
    """project permissions."""
    return Permission.objects.get(
        name='Has a my Project Page',
        codename='has_project',
        content_type=admin_ct())


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
