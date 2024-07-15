from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout

from .forms import *
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


def login_view(request):
	if request.method == 'GET':
		return render(request, 'base/login.html', {
			'form': LoginForm()
		})

	elif request.method == 'POST':
		login_ = request.POST.get('login')
		password_ = request.POST.get('password')

		usr = authenticate(request, username=login_, password=password_)

		if usr is not None:
			user_login(request, usr)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'base/login.html', {
				'form': LoginForm(request.POST)
			})


def reg_view(request):
	if request.method == 'GET':
		return render(request, 'base/register.html', {
			'form': RegForm()
		})
	else:
		form = RegForm(request.POST)
		error = ''

		login = request.POST.get('login')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')
		email = request.POST.get('email')

		if form.is_valid():
			if password != password2:
				error = 'Введённые пароли не совпадают!\n'
			if CustomUser.objects.filter(email=email).exists():
				error = 'Введённый адрес электронной почты занят!\n'
			if CustomUser.objects.filter(username=login).exists():
				error = 'Пользователь с таким логином уже существует!\n'

			if error:
				return render(request, 'base/register.html', {
					'form': form,
					'error': error
				})

			else:
				new_user = CustomUser.objects.create(
					username=login,
					email=email
				)

				new_user.set_password(password)
				new_user.save()

				return HttpResponseRedirect('/login')


def logout(request):
	user_logout(request)
	return HttpResponseRedirect('/')
