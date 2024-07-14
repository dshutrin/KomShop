from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *


# Create your views here.
def get_first_page(request):
	return HttpResponseRedirect('/catalog/page_1')


def home(request, page):

	limit = 10

	products = Product.objects.all()[(limit*(page-1)):(limit*page)]

	prev_page = None
	next_page = None

	if page > 1:
		prev_page = page - 1

	if Product.objects.all().count() > (page * limit):
		next_page = page + 1

	return render(request, 'base/home.html', {
		'products': products,
		'limit': limit,
		'current_page': page,
		'prev_page': prev_page,
		'next_page': next_page
	})
