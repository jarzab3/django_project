from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from regression import views
from regression import forms


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^main$', views.main, name='main'),
    url(r'^create$', views.user_story_post_create, name='us_post_create'),
    url(r'^display_us$', views.display_us_subject, name='display_us_subject'),
    url(r'^modal_detail_view/(?P<id>\d+)', views.modal_detail_view, name='modal_detail_view'),

    #Below unused
    
    # url(r'^display_us/(?P<pk>\d+)/', views.user_story_detail_view, name='display_us_details'),
    # url(r'^tables$', views.tables, name='tables'),
    # #url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^submitted$', views.submitted, name='subject_to_change'),
    #
    # ]
    # url(r'^$', views.index, name='index'),
    # url(r'^index.html$', views.index, name='index'),
    # url(r'^charts.html$', views.charts, name='charts'),
    # url(r'^tables.html$', views.tables, name='tables'),
    # url(r'^forms.html$', views.AddNewUserStory_view, name='AddNewUserStory_view'),
    # url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^form_upload.html$', views.submitted, name='subject_to_change'),
    # url(r'^login/', views.login, name = 'login'),
    # url(r'^connection/',TemplateView.as_view(template_name = 'regression/login.html')),


]


# urlpatterns = patterns('regression.views',
#    url(r'^$', views.index, name='index'),
#    url(r'^index.html$', views.index, name='index'),
#    url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
#    url(r'^login/', 'login', name = 'login'))
