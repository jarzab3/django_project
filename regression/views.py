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
from regression.forms import CategoryForm as CatForm

from regression.models import UserStory
from regression.models import Category

logger = logging.getLogger(__name__)

@login_required(login_url="login/")
def home(request):
    return render(request, "index.html")


@login_required(login_url="login/")
def manage(request):
    return render(request, "manage.html")


@login_required(login_url="login/")
def display_us_subject(request):
    try:
        all_user_stories = UserStory.objects.all()
        data = all_user_stories
        data.is_us = True
        logger.info("Displayed all us stories")
    except Exception as error:
        logger.info("Error when display user story. %s", error)

    return render(request, 'display_us_cat.html', {
        'data': data
    })


@login_required(login_url="login/")
def display_category_subject(request):
    try:
        all_categories = Category.objects.all()
        data = all_categories
        data.is_category = True
        logger.info("Displayed all categories")
    except Exception as error:
        logger.info("Error when display categories. %s", error)

    return render(request, 'display_us_cat.html', {
        'data': data
    })



@login_required(login_url="login/")
def user_story_post_create(request):
    """Create a new user story
    Handle the form GET and POST
    """

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
                instance.created_by = request.user

                logger.debug("user %s" % request.user)

                instance.case_title = form['case_title'].value().capitalize()

                instance.repro_steps = form['repro_steps'].value().capitalize()

                # form['repro_steps'].value().capitalize()
                # form['test_preconditions'].value().capitalize()
                # form['extra_notes'].value().capitalize()

                # logger.info("Values from request: %s " % cap_case_title)
                # logger.info("Values 222 from request: %s" % form.data['repro_steps'])

                instance.save()

                form = USForm()

                messages.success(request, 'User story successfully added')

            except Exception as error:
                error_message = 'Something happened during the save of the user story: %s' % error
                messages.error(request, error_message)
                pass

    return render(request, 'add_user_story.html', {
        "form": form,
    })


@csrf_exempt
@login_required(login_url="login/")
def category_post_create(request):
    """Create a new category
    Handle the form GET and POST
    """

    if request.method == 'GET':
        # Handle the request of a form
        # Here you can manage and edit if you have the instance value.
        form = CatForm()

    if request.method == 'POST':
        # Handle the data sent by the form
        form = CatForm(request.POST)

        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.created_by = request.user
                instance.save()

                logger.info("user %s" % request.user)


                form = CatForm()

                messages.success(request, 'New category successfully added')

            except Exception as error:
                error_message = 'Something happened during the save of the category: %s' % error
                messages.error(request, error_message)
                pass

    return render(request, 'add_category.html', {
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


@login_required(login_url="login/")
def view_backlog(request):
    try:
        all_categories = Category.objects.all()
        data = all_categories
        data.is_category = True
        # logger.info("")

    except Exception as error:
        logger.info("Error while attempt to display backlog. %s", error)

    return render(request, 'view_backlog.html', {
        'data': data
    })

