from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^home/$', home_page, name='home_page'),
    url(r'^projectlist/$', project_list, name='project_list'),
    url(r'^projectdetails/([0-9]+)/', project_details, name='project_details'),
    url(r'^studentlist/$', student_list, name='student_list'),
    url(r'^schoollist/$', school_list, name='school_list'),
    url(r'^employeelist/$', employee_list, name='employee_list'),
    url(r'^profile/[0-9]+/', user_profile, name='user_profile'),
    url(r'^addSchool/$', add_school, name='add_school'),
    url(r'^addemployee/$', add_employee, name='add_employee'),

]
