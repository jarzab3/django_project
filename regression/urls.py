#!python
# regression/urls.py

from django.conf.urls import include, url
from django.contrib import admin
# from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from regression import views
from regression import forms

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^add_story$', views.user_story_post_create, name='us_post_create'),
    url(r'^add_category$', views.category_post_create, name='category_post_create'),
    url(r'^view_all$', views.display_us_subject, name='display_us_subject'),
    # url(r'^view_categories$', views.display_us_subject, name='display_us_subject'),
    url(r'^manage$', views.manage, name='manage'),
    url(r'^modal_detail_view/(?P<id>\d+)', views.modal_detail_view, name='modal_detail_view')
    ]