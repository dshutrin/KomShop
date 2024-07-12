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
	path('admin_panel/delete_product/<int:id>', admin_panel_delete_product),
	path('admin_panel/products/edit/<int:id>', admin_panel_edit_product),
	path('admin_panel/tag_make_product', tag_make_product),
	path('admin_panel/tag_make_other', tag_make_other),
	path('admin_panel/cat_make_product', cat_make_product),
	path('admin_panel/cat_make_other', cat_make_other),
	path('admin_panel/tags/add', add_tag)
]


urlpatterns = [
	path('', home)
] + admin_panel_urlpatterns
