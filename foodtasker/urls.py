from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from foodtaskerapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^restaurant/sign-in/$',auth_views.login,
        {'template_name' : 'restaurant/sign_in.html'},
        name = 'restaurant-sign-in'),
    url(r'^restaurant/sign-out',auth_views.logout,
        {'next_page' : '/restaurant/sign-in/'},
        name = 'restaurant-sign-out'),
    url(r'^restaurant/$',views.restaurant_home,name = "restaurant-home")
]
