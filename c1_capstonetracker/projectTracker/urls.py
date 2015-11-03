from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', home_page, name='home_page'),
    url(r'^projectlist/$', project_list, name='project_list'),
    url(r'^projectdetails/([0-9]+)/', project_details, name='project_details'),
    url(r'^studentlist/$', student_list, name='student_list'),
]
