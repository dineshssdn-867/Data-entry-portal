from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'login'
urlpatterns = [
    path('', main_view, name="index"),
    path('home',login_vew,name="login"),
    path('logout',logout_request,name='logout')
]
