from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('main', home_view, name="main"),
    path('entryportal',portal_view,name="portal"),
    path('portal', entry_view, name="entry"),
    path('camera',camera_view,name="camera"),
    path('view', view_entry,name="view"),
    path('delete/<int:id>',delete_entry,name="delete"),
    path('logout',logout_request,name='logout'),
    path('update/<int:id>',update_entry,name="update")
]
