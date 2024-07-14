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
	lf_page = None
	rf_page = None

	if page > 1:
		prev_page = page - 1

	if Product.objects.all().count() > (page * limit):
		next_page = page + 1

	if page > 5:
		lf_page = page - 5
	else:
		if page > 2:
			lf_page = 1

	if (Product.objects.all().count() / limit) - page > 5:
		rf_page = page + 5
	elif page != round(Product.objects.all().count() / limit):
		rf_page = round(Product.objects.all().count() / limit) + 1

	if page == rf_page:
		rf_page = None

	return render(request, 'base/home.html', {
		'products': products,
		'limit': limit,
		'current_page': page,
		'prev_page': prev_page,
		'next_page': next_page,
		'lf_page': lf_page,
		'rf_page': rf_page,
	})
