from django.contrib import admin

from .models import Post


class AdminPost(admin.ModelAdmin):
    list_filter = ['full_Name']
    search_fields = ['full_Name']

    class meta:
        model = Post


admin.site.register(Post, AdminPost)
