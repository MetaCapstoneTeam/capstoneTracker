from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('frontend.urls', namespace='frontend',
        app_name='frontend')),
    url(r'^projectTracker/', include('projectTracker.urls')),
    url(r'^login/$', 'projectTracker.views.login_user'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
]
