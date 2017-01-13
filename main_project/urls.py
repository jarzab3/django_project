from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from regression import views
from regression import forms


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^display_us/(?P<pk>\d+)/', views.user_story_detail_view, name='display_us_details'),
    url(r'^tables$', views.tables, name='tables'),
    url(r'^display_us$', views.display_us_subject, name='display_us_subject'),
    #url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form_upload.html$', views.submitted, name='subject_to_change'),
    url(r'^create$', views.post_create, name='post_create'),
    ]
