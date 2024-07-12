from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):

	limit = 100
	products = Product.objects.all()[:limit]

	return render(request, 'base/home.html', {
		'products': products,
		'limit': limit
	})
