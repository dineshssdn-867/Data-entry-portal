from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Darbar


class AdminPost(admin.ModelAdmin):
    list_filter = ['full_Name']
    search_fields = ['full_Name']

    class meta:
        model = Post


class DarbarPost(admin.ModelAdmin):
    list_filter = ['darbar_city']
    search_fields = ['darbar_city']

    class meta:
        model = Darbar

admin.site.register(Post, AdminPost)
admin.site.register(Darbar, DarbarPost)