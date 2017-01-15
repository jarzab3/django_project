import logging

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

from regression.serializers import UserStorySerializer
from regression.forms import UserStoryForm
from regression.models import UserStory

logger = logging.getLogger(__name__)


def main(request):
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

def charts(request):
    return render(request, 'regression/charts.html', {
    })



def display_us_subject(request):
    try:
        all_user_stories = UserStory.objects.all()
        data = all_user_stories
    except Exception as error:
        logger.info("Display user story error. %s", error)

    return render(request, 'regression/display_us.html', {
        'data': data
    })


@csrf_exempt
def user_story_post_create(request):
    """Create a new user story

    Handle the form GET and POST
    """
    if request.method == 'GET':
        # handle the request of a form
        # here you can manage and edit if you have the instance value.
        form = PostForm()

    if request.method == 'POST':
        # Handle the data sent by the form
        form = PostForm(request.POST)

        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.save()
                messages.success('User story %s correctly saved' % instance.subject)

            except Exception as error:
                error_message = 'Something happened during the save of the user story: %s' % error
                messages.error(request, error_message)

    return render(request, 'regression/us_post_form.html', {
    	"form": form, 
    	})


#List all user stories 


@api_view(['GET'])
def user_story_detail_view(request):
    if request.method == 'GET':
        user_stories = UserStory.objects.all()
        serializer = UserStorySerializer(user_stories, many=True)
        return Response(serializer.data)

