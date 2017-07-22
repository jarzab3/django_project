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

# #!python
# # log/urls.py
# from django.conf.urls import url
# from . import views


@login_required(login_url="login/")
def home(request):
    return render(request, "index.html")

@login_required(login_url="login/")
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
@login_required(login_url="login/")
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

                messages.success(request, 'User story successfully added')

            except Exception as error:
                error_message = 'Something happened during the save of the user story: %s' % error
                messages.error(request, error_message)
                pass

    return render(request, 'us_post_form.html', {
    	"form": form, 
    	})

def modal_detail_view(request, id):
	try:
		user_story = UserStory.objects.get(id=id)
	except UserStory.DoesNotExist:
		raise Http404('This user_story does not exist')
	return render(request, 'modal_detail_view.html', {
	'user_story': user_story,
	})


def user_story_detail_view(request, id):
    return HttpResponse('<p> In item_detail view with pk {0}</p>'.format(id))

