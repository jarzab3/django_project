from django.conf.urls import include, url
from django.contrib import admin

from regression import views
from regression import forms

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^charts.html$', views.charts, name='charts'),
    url(r'^tables.html$', views.tables, name='tables'),
    url(r'^forms.html$', forms.forms, name='forms'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
