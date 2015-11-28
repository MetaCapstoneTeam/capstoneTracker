"""from django.db.models import signals
from django.contrib.auth.models import Group, Permission
import models 

projectTracker_group_permissions = {
  "Administrator_User": [
    "can_add_student",
    "can_view_students",
    "can_add_employee",
    "can_view_employees",        
    "can_add_school",
    "can_view_schools",
    "can_add_project",
    "can_view_projects", 
    "can_add_team",
    "can_view_teams",
    ],
  "Employee_User": [
    "can_view_projects",
    "can_view_employees",
    "can_view_schools",
    "can_view_teams",

    ],
  "Student_User": [ 
    ],
}

def create_user_groups(app, created_models, verbosity, **kwargs):
  if verbosity>0:
    print "Initialising data post_syncdb"
  for group in projectTracker_group_permissions:
    role, created = Group.objects.get_or_create(name=group)
    if verbosity>1 and created:
      print 'Creating group', group
    for perm in projectTracker_group_permissions[group]: 
      role.permissions.add(Permission.objects.get(codename=perm))
      if verbosity>1:
        print 'Permitting', group, 'to', perm
    role.save()

signals.post_syncdb.connect(
  create_user_groups, 
  sender=models, 
  dispatch_uid='projectTracker.models.create_user_groups'
  )"""