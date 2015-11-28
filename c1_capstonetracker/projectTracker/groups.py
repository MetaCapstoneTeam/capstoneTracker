from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


administrative_users,_ = Group.objects.get_or_create(name='Administrative Users')
administrative_users.save()

employee_users,_ = Group.objects.get_or_create(name='Employee Users')
employee_users.save()

student_users,_ = Group.objects.get_or_create(name='Student Users')
student_users.save()


admin_ct = ContentType.objects.get(app_label='projectTracker', model='Administrator')
student_ct = ContentType.objects.get(app_label='projectTracker', model='Student')

can_view_students,_ = Permission.objects.get_or_create(name='Can View Students', codename='can_view_students',
                       content_type=admin_ct)
can_view_students.save()

can_view_employees,_ = Permission.objects.get_or_create(name='Can View Employees', codename='can_view_employees',
                       content_type=admin_ct)
can_view_employees.save()

can_view_projects,_ = Permission.objects.get_or_create(name='Can View Projects', codename='can_view_projects',
                       content_type=admin_ct)
can_view_projects.save()

can_view_teams,_ = Permission.objects.get_or_create(name='Can View Teams', codename='can_view_teams',
                       content_type=admin_ct)
can_view_teams.save()

can_view_schools,_ = Permission.objects.get_or_create(name='Can View Schools', codename='can_view_schools',
                       content_type=admin_ct)
can_view_schools.save()

can_edit_students,_ = Permission.objects.get_or_create(name='Can Edit Students ', codename='can_edit_students',
                       content_type=admin_ct)
can_edit_students.save()

can_edit_schools,_ = Permission.objects.get_or_create(name='Can Edit Schools ', codename='can_edit_schools',
                       content_type=admin_ct)
can_edit_schools.save()

can_edit_employees,_ = Permission.objects.get_or_create(name='Can Edit Employees ', codename='can_edit_employees',
                       content_type=admin_ct)
can_edit_employees.save()

can_edit_teams,_ = Permission.objects.get_or_create(name='Can Edit Teams ', codename='can_edit_teams',
                       content_type=admin_ct)
can_edit_teams.save()

can_edit_projects,_ = Permission.objects.get_or_create(name='Can Edit Projects ', codename='can_edit_projects',
                       content_type=admin_ct)
can_edit_projects.save()

has_student_profile,_ = Permission.objects.get_or_create(name='Is A Student User', codename='has_student_profile',
						content_type=admin_ct)
has_student_profile.save()

has_employee_profile,_ = Permission.objects.get_or_create(name='Is an Employee User', codename='has_employee_profile',
						content_type=admin_ct)


administrative_users.permissions = [can_view_teams, can_edit_teams,
									can_view_projects, can_edit_projects,
									can_view_employees, can_edit_employees,
									can_view_students, can_edit_students,
									can_view_schools, can_edit_schools]

employee_users.permissions = [can_view_teams, can_view_projects, can_view_employees, can_view_students, can_view_schools, has_employee_profile]

student_users.permissions = [has_student_profile]