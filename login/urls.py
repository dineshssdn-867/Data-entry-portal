from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', main_view, name="index"),
    path('register',register_view,name="register"),
    path('home',login_vew,name="login"),
    path('logout',logout_request,name='logout')
]
