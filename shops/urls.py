from django.urls import path
from . import views

urlpatterns = [
 path('', views.product_list, name='product_list'),
 path('<slug:category_slug>/', views.product_list,
        name='product_list_by_category'),
 path('<int:id>/<slug:slug>/', views.product_detail,
        name='product_detail'),

path(r'^cart/$', views.cart),
path(r'^additem/(\d+)/(\d+)/$', views.add_to_cart, name='additem-url'),
path(r'^removeitem/(\d+)/$', views.remove_from_cart, name='removeitem-url'),



]