from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django import forms
from django.views import generic
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from regression.models import user_story
from regression.forms import PostForm
import ipdb
import logging

logger = logging.getLogger('loggly_logs')


def index(request):
	return render(request, 'regression/index.html', {
	})




def submitted(request):
	return render(request, 'regression/submitted.html', {
	})


def forms(request):
	return render(request, 'regression/forms.html', {   
	})

def tables(request):
	return render(request, 'regression/tables.html', {   
	})



def display_us_subject(request):
	try:
	    all_user_stories = user_story.objects.all()
	    data = all_user_stories
	except Exception as error:
		logger.info("Display user story error. %s" %(ipdb.set_trace()))

	return render(request, 'regression/display_us.html', {
    	'data': data
    	})

def post_create(request):
	form = PostForm(request.POST or None)
	var = False
	if form.is_valid():
		try:
			instance = form.save(commit=False)
			instance.save()
			print form.cleaned_data.get("subject")
			print form.cleaned_data.get("case_title")
			#print form.cleaned_data.get("content")
			#instance.save()
			var = True
		except Exception as error:
			logger.DEBUG("Post form error. %s" %(ipdb.set_trace()))

	context = {
		"form": form,
	}

	return render(request, "regression/post_form.html", context, var )


def charts(request):
	return render(request, 'regression/charts.html', {
	})


def user_story_detail_view(request, pk):
	return HttpResponse('<p> In item_detail view with pk {0}</p>'.format(pk))
