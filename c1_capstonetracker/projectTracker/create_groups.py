from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


administrative_users = Group.objects.create(
    name='Administrative Users')
administrative_users.save()

employee_users = Group.objects.create(
    name='Employee Users')
employee_users.save()

student_users = Group.objects.create(
    name='Student Users')
student_users.save()


admin_ct = ContentType.objects.get(app_label='projectTracker',
                                   model='Administrator')
student_ct = ContentType.objects.get(app_label='projectTracker',
                                     model='Student')

can_view_students = Permission.objects.create(
    name='Can View Students',
    codename='can_view_students',
    content_type=admin_ct)
can_view_students.save()

can_view_employees = Permission.objects.create(
    name='Can View Employees',
    codename='can_view_employees',
    content_type=admin_ct)
can_view_employees.save()

can_view_projects = Permission.objects.create(
    name='Can View Projects',
    codename='can_view_projects',
    content_type=admin_ct)
can_view_projects.save()

can_view_teams = Permission.objects.create(
    name='Can View Teams',
    codename='can_view_teams',
    content_type=admin_ct)
can_view_teams.save()

can_view_schools = Permission.objects.create(
    name='Can View Schools',
    codename='can_view_schools',
    content_type=admin_ct)
can_view_schools.save()

can_view_admins = Permission.objects.create(
    name='Can View Administrators',
    codename='can_view_admins',
    content_type=admin_ct)
can_view_admins.save()


can_edit_students = Permission.objects.create(
    name='Can Edit Students ',
    codename='can_edit_students',
    content_type=admin_ct)
can_edit_students.save()

can_edit_schools = Permission.objects.create(
    name='Can Edit Schools ',
    codename='can_edit_schools',
    content_type=admin_ct)
can_edit_schools.save()

can_edit_employees = Permission.objects.create(
    name='Can Edit Employees ',
    codename='can_edit_employees',
    content_type=admin_ct)
can_edit_employees.save()

can_edit_teams = Permission.objects.create(
    name='Can Edit Teams ',
    codename='can_edit_teams',
    content_type=admin_ct)
can_edit_teams.save()

can_edit_projects = Permission.objects.create(
    name='Can Edit Projects ',
    codename='can_edit_projects',
    content_type=admin_ct)
can_edit_projects.save()

can_edit_admins = Permission.objects.create(
    name='Can Edit Administrators ',
    codename='can_edit_admins',
    content_type=admin_ct)
can_edit_admins.save()

has_student_profile = Permission.objects.create(
    name='Is A Student User',
    codename='has_student_profile',
    content_type=admin_ct)
has_student_profile.save()

has_employee_profile = Permission.objects.create(
    name='Is an Employee User',
    codename='has_employee_profile',
    content_type=admin_ct)
has_employee_profile.save()

has_project = Permission.objects.create(
    name='Has a my Project Page',
    codename='has_project',
    content_type=admin_ct)
has_project.save()
