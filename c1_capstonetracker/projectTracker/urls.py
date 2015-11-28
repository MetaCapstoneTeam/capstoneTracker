from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^home/$', home_page, name='home_page'),
    url(r'^projectlist/$', project_list, name='project_list'),
    url(r'^myproject/[0-9]+/', my_project, name='my_project'),
    url(r'^studentlist/$', student_list, name='student_list'),
    url(r'^schoollist/$', school_list, name='school_list'),
    url(r'^employeelist/$', employee_list, name='employee_list'),
    url(r'^teamlist/$', team_list, name='team_list'),
    url(r'^profile/([0-9]+)/', user_profile, name='user_profile'),
    url(r'^addSchool/$', add_school, name='add_school'),
    url(r'^addemployee/$', add_employee, name='add_employee'),
    url(r'^addstudent/$', add_student, name='add_student'),
    url(r'^addproject/$', add_project, name='add_project'),
    url(r'^addTeam/$', add_team, name='add_team'),
    url(r'^$', logout_user, name='logout_user'),
]
