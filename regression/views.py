import logging

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

# from regression.serializers import UserStorySerializer
from regression.forms import UserStoryForm as USForm

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
    form = USForm()

    if request.method == 'GET':
        # handle the request of a form
        # here you can manage and edit if you have the instance value.
        form = USForm()

    if request.method == 'POST':
        # Handle the data sent by the form
        form = USForm(request.POST)

        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.save()
                form = USForm()
            #subject = form.cleaned_data['subject_f', '']
            #case_title = form.cleaned_data['case_title_f', '']
            #post = m.Post.objects.create(content=content,
             #                            created_at=created_at)
            logger.info('reguest.POST')
            subject = request.POST.get('subject_f', '')
            case_title = request.POST.get('case_title_f', '')

            user_story_object = user_story(subject=subject, case_title=case_title)
            user_story_object.save()
            #return HttpResponseRedirect(reverse('post_detail',
            #                                    kwargs={'post_id': post.id}))


                messages.success(request, 'User story %s correctly saved' % instance.subject)

            except Exception as error:
                pass
                error_message = 'Something happened during the save of the user story: %s' % error
                messages.error(request, error_message)

    return render(request, 'regression/us_post_form.html', {
    	"form": form, 
    	})



def user_story_detail_view(request, id):
    return HttpResponse('<p> In item_detail view with pk {0}</p>'.format(id))

def modal_detail_view(request, id):
	try:
		user_story = UserStory.objects.get(id=id)
	except UserStory.DoesNotExist:
		raise Http404('This user_story does not exist')
	return render(request, 'regression/modal_detail_view.html', {
	'user_story': user_story,
	})
