"""
URL configuration for Ordering_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Ordering_System_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('shop', views.shop),
    path('contact', views.contact),
    path('shop-details/<int:id>', views.shop_details),
    path('add/<int:dish_id>/', views.add_to_cart),
    path('remove/<int:dish_id>/', views.remove_from_cart),
    path('shoping-cart', views.shoping_cart),
    path('checkout', views.checkout),
    path('restaurant', views.restaurant),
    path('dishes', views.dishes),
    path('dishesCategory/<int:id>', views.dishCategory),
    path('restaurantsCategory/<int:id>', views.resCategory),
    path('search_dish', views.searchbar_dish),
    path('search_restaurant', views.searchbar_res),
    path('restaurant-details/<int:id>', views.restaurant_details),
    # path('download/<int:file_id>/', views.download_file),
    path('user_login', views.user_login),
    path('restaurant-register', views.create_restaurant),
    path('user_signup', views.sign_up),
    path('user_logout', views.user_logout),

    # For CRUD Operations

    # path('contact', views.Create),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)