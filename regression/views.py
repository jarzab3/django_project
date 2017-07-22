import logging
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from rest_framework.response import Response
from rest_framework.decorators import api_view

# from regression.serializers import UserStorySerializer
from regression.forms import UserStoryForm as USForm

from regression.models import UserStory

logger = logging.getLogger(__name__)

#!python
# log/urls.py
from django.conf.urls import url
from . import views

# @login_required(login_url="login/")
# def home(request):
#     return render(request, "regression/index.html")

@login_required(login_url="login/")
def home(request):
    return render(request, "index.html")


# def login(request):
#     return render(request, 'regression/login.html', {
#     })
#
# def main(request):
#     return render(request, 'regression/index.html', {
#     })




# def submitted(request):
#     return render(request, 'regression/submitted.html', {
#     })
#
# def forms(request):
#     return render(request, 'regression/forms.html', {
#     })

#
# def tables(request):
#     return render(request, 'regression/tables.html', {
#     })
#
# def charts(request):
#     return render(request, 'regression/charts.html', {
#     })

def display_us_subject(request):
    try:
        all_user_stories = UserStory.objects.all()
        data = all_user_stories
        logger.debug('Fetch user stories and display to website successfully!')
    except Exception as error:
        logger.info("Error when display user story. %s", error)

    return render(request, 'display_us.html', {
        'data': data
    })


@csrf_exempt
def user_story_post_create(request):
    """Create a new user story

    Handle the form GET and POST
    """
    # form = USForm()

    if request.method == 'GET':
        # Handle the request of a form
        # Here you can manage and edit if you have the instance value.
        form = USForm()

    if request.method == 'POST':
        # Handle the data sent by the form
        form = USForm(request.POST)

        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.save()
                form = USForm()

                messages.success(request, 'User story %s correctly saved' % instance.subject)

            except Exception as error:
                error_message = 'Something happened during the save of the user story: %s' % error
                messages.error(request, error_message)
                pass

    return render(request, 'us_post_form.html', {
    	"form": form, 
    	})


def user_story_detail_view(request, id):
    return HttpResponse('<p> In item_detail view with pk {0}</p>'.format(id))

def modal_detail_view(request, id):
	try:
		user_story = UserStory.objects.get(id=id)
	except UserStory.DoesNotExist:
		raise Http404('This user_story does not exist')
	return render(request, 'modal_detail_view.html', {
	'user_story': user_story,
	})


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')

    # return render_to_response('regression/login.html', context_instance=RequestContext(request))

    return render(request, 'login.html', {
        # 'data': "logged"
    })
#
#
