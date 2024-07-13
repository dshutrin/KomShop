from django.urls import path
from .admin_panel_views import *
from .views import *


admin_panel_urlpatterns = [
	path('admin_panel', admin_panel),
	path('admin_panel/roles', admin_panel_roles),
	path('admin_panel/categories', admin_panel_product_categories),
	path('admin_panel/tags', admin_panel_tags),
	path('admin_panel/products', admin_panel_products),
	path('admin_panel/products/add', admin_panel_products_add),
	path('admin_panel/delete_product/<int:pid>', admin_panel_delete_product),
	path('admin_panel/products/edit/<int:pid>', admin_panel_edit_product),
	path('admin_panel/remove_tag', admin_panel_remove_product_tag),
	path('admin_panel/add_tag', admin_panel_add_product_tag),

	path('admin_panel/remove_cat', admin_panel_remove_product_cat),
	path('admin_panel/add_cat', admin_panel_add_product_cat)
]


urlpatterns = [
	path('', home)
] + admin_panel_urlpatterns
