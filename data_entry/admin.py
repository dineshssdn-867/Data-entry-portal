from django.conf import settings
from django.contrib import admin

from .models import Post


class AdminPost(admin.ModelAdmin):
    list_filter = ['full_Name']
    search_fields = ['full_Name']


    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('CSS/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/location_picker.js',
            )

    class meta:
        model = Post


admin.site.register(Post, AdminPost)
