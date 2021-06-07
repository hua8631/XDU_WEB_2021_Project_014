"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from shops.urls import urlpatterns as shopsurl
from cart.urls import urlpatterns as cartsurl
from orders.urls import urlpatterns as ordersurl
urlpatterns = [

    path('admin/', admin.site.urls),
    path('shops/', include((shopsurl,'shops'), namespace='shops')),
    path('cart/', include((cartsurl,'cart'), namespace='cart')),
    path('orders/', include((ordersurl, 'orders'), namespace='orders')),
    path('', include((shopsurl,'shops'), namespace='a')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)