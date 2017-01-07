from django.shortcuts import render
from django.http import Http404
from django import forms

from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView

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


#from regression.models import Cost
from regression.forms import CostForm


def tables(request):	
	#form = CostForm()
	form = CostForm(request.POST)

	#logger.info(request.method)
	if form.is_valid():
		con = form.cleaned_data['fields']
		logger.info(con)
		logger.info("here")
	


	

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

from regression.forms import PostForm
from regression.models import Post


def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print form.cleaned_data.get("title")
		print form.cleaned_data.get("content")
		instance.save()
	# if request.method == "POST":
	# 	print (request.POST.get("content"))
	# 	print (request.POST.get("title"))

	context = {
		"form": form,

	}
	return http.HttpResponseRedirect('')
	#return render(request, "regression/post_form.html", context)


def post_detial(request, id=None):

	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instancem
	}
	return render(request, "post_detail.html", context)


def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}