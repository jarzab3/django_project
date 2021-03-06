#!python
# main_project/urls.py

from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from regression.forms import LoginForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('regression.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'session_security/', include('session_security.urls'))
]
