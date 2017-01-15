from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from regression import views
from regression import forms


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^main$', views.main, name='main'),
    url(r'^create$', views.user_story_post_create, name='us_post_create'),
    url(r'^display_us$', views.display_us_subject, name='display_us_subject'),
    
    #Below unused
    
    url(r'^us_detail_view', views.user_story_detail_view),
    url(r'^tables$', views.tables, name='tables'),
    #url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^submitted$', views.submitted, name='subject_to_change'),
    
    ]
urlpatterns = format_suffix_patterns(urlpatterns)