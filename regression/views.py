from django.shortcuts import render
from django.http import Http404

from regression.models import Item


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



def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'regression/item_detail.html', {
		'item': item,
	})
