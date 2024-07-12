from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt


@login_required
def admin_panel(request):
	if request.user.role.access_to_admin_panel:

		return render(request, 'admin_panel/home.html')

	else:
		return HttpResponseNotFound(request)


@login_required
def admin_panel_roles(request):
	if request.user.role.access_to_admin_panel:

		roles = Role.objects.all()

		return render(request, 'admin_panel/roles.html', {
			'roles': roles
		})

	else:
		return HttpResponseNotFound(request)


@login_required
def admin_panel_product_categories(request):
	if request.user.role.access_to_admin_panel:

		categories = Category.objects.all()

		return render(request, 'admin_panel/product_categories.html', {
			'categories': categories
		})

	else:
		return HttpResponseNotFound(request)


@login_required
def admin_panel_tags(request):
	if request.user.role.access_to_admin_panel:

		tags = Tag.objects.all()

		return render(request, 'admin_panel/tags.html', {
			'tags': tags
		})

	else:
		return HttpResponseNotFound(request)


@login_required
def admin_panel_products(request):
	if request.user.role.access_to_admin_panel:

		products = Product.objects.all()

		return render(request, 'admin_panel/products.html', {
			'products': products
		})

	else:
		return HttpResponseNotFound(request)


@login_required
def admin_panel_products_add(request):
	if request.user.role.access_to_admin_panel:
		form = ProductForm()
		if request.method == 'GET':
			return render(request, 'admin_panel/product_add.html', {
				'form': form
				})
		else:
			form = ProductForm(request.POST, request.FILES)
			if form.is_valid:
				form.save()
				return HttpResponseRedirect('/admin_panel/products')
	else:
		return HttpResponseNotFound(request)


def admin_panel_delete_product(request, id):
	Product.objects.get(id=id).delete()
	return HttpResponseRedirect('/admin_panel/products')


@login_required
def admin_panel_edit_product(request, id):
	if request.user.role.access_to_admin_panel:
		product = Product.objects.get(id=id)
		form = ProductForm(request.POST, request.FILES, instance=product)
		if request.method == 'GET':
			return render(request, 'admin_panel/product_edit.html', {
				'form': ProductForm(instance=product),
				'tags': Tag.objects.all(),
				'categories': Category.objects.all(),
				'product_tags': product.tags,
				'product_categories': product.categories,
				'other_tags': Tag.objects.all().exclude(product=product),
				'other_categories': Category.objects.all().exclude(product=product)
				})
		else:
			if form.is_valid:
				product = form.save()

				return HttpResponseRedirect('/admin_panel/products')
	else:
		return HttpResponseNotFound(request)



@csrf_exempt
def tag_make_other(request):
	tag_id = request.POST.get('tag_id')
	prod_id = request.POST.get('prod_id')
	product = Product.objects.get(id=prod_id)
	tag = Tag.objects.get(id=tag_id)
	product.tags.remove(tag)
	return render(request, 'admin_panel/product_edit.html', {
		'form': ProductForm(instance=product),
		'tags': Tag.objects.all(),
		'categories': Category.objects.all(),
		'product_tags': product.tags,
		'product_categories': product.categories,
		'other_tags': Tag.objects.all().exclude(product=product),
		'other_categories': Category.objects.all().exclude(product=product)
	})


@csrf_exempt
def cat_make_product(request):
	cat_id = request.POST.get('cat_id')
	prod_id = request.POST.get('prod_id')
	product = Product.objects.get(id=prod_id)
	cat = Category.objects.get(id=cat_id)
	product.tags.add(cat)
	return render(request, 'admin_panel/product_edit.html', {
		'form': ProductForm(instance=product),
		'tags': Tag.objects.all(),
		'categories': Category.objects.all(),
		'product_tags': product.tags,
		'product_categories': product.categories,
		'other_tags': Tag.objects.all().exclude(product=product),
		'other_categories': Category.objects.all().exclude(product=product)
	})


@csrf_exempt
def cat_make_other(request):
	cat_id = request.POST.get('cat_id')
	prod_id = request.POST.get('prod_id')
	product = Product.objects.get(id=prod_id)
	cat = Category.objects.get(id=cat_id)
	product.tags.remove(cat)
	return render(request, 'admin_panel/product_edit.html', {
		'form': ProductForm(instance=product),
		'tags': Tag.objects.all(),
		'categories': Category.objects.all(),
		'product_tags': product.tags,
		'product_categories': product.categories,
		'other_tags': Tag.objects.all().exclude(product=product),
		'other_categories': Category.objects.all().exclude(product=product)
	})

@csrf_exempt
def tag_make_product(request):
	tag_id = request.POST.get('tag_id')
	prod_id = request.POST.get('prod_id')
	product = Product.objects.get(id=prod_id)
	tag = Tag.objects.get(id=cat_id)
	product.tags.add(tag)
	return render(request, 'admin_panel/product_edit.html', {
		'form': ProductForm(instance=product),
		'tags': Tag.objects.all(),
		'categories': Category.objects.all(),
		'product_tags': product.tags,
		'product_categories': product.categories,
		'other_tags': Tag.objects.all().exclude(product=product),
		'other_categories': Category.objects.all().exclude(product=product)
	})


@login_required
def add_tag(request):
	if request.user.role.access_to_admin_panel:
		form = TagForm()
		if request.method == 'GET':
			return render(request, 'admin_panel/tag_add.html', {
				'form': form
				})
		else:
			form = TagForm(request.POST)
			if form.is_valid:
				form.save()
				return HttpResponseRedirect('/admin_panel/tags')
	else:
		return HttpResponseNotFound(request)