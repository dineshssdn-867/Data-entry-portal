from django.urls import path
from .views import *

app_name = 'login'
urlpatterns = [
    path('home/', main_view, name="index"),
    path('', login_vew, name="login"),
    path('logout/', logout_request, name='logout')
]
