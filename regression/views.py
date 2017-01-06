from django.shortcuts import render
from django.http import Http404
from django import forms

from django.http import HttpResponseRedirect

from regression.models import Item

import logging
logger = logging.getLogger('loggly_logs')


def index(request):
	items = Item.objects.exclude(amount=0)
	return render(request, 'regression/index.html', {
		'items': items,
	})


def charts(request):
	items = Item.objects.exclude(amount=0)
	return render(request, 'regression/charts.html', {
		'items': items,
	})

def submitted(request):
	return render(request, 'regression/submitted.html', {
	})


def forms(request):
	return render(request, 'regression/forms.html', {
        
	})


from regression.models import Cost
from regression.forms import CostForm


def tables(request):
	logger.info("here")
	form = CostForm()
	
	cost_var = request.POST.get('cost')
	logger.info(cost_var)


	return render(request, 'regression/tables.html', {
		'form': form
	})



def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'regression/item_detail.html', {
		'item': item,
	})


from regression.models import user_story

from regression.forms import AddNewUserStory





def AddNewUserStory_view(request):
    if request == 'POST':
        #form = PostForm()

        # A POST request: Handle Form Upload
        form = AddNewUserStory(request.POST) # Bind data from request.POST into a PostForm
        logger.info('before valid')
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
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

            return HttpResponseRedirect(reverse('regression:user_story'))
    else:
    	form = AddNewUserStory()



    return render(request, 'regression/forms.html', {
        'form': form,
    })

#eturn render(request, "regression/forms.html", {'form': AddNewUserStory()})