from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Account


class MyAdminAccounts(UserAdmin):
    model = Account
    list_display = ('email', 'city')
    list_filter = ('email', 'city')
    search_fields = ('email', 'city')
    ordering = ('email', 'city')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'city', 'is_staff', 'is_admin', 'is_data_entry', 'is_active')
        }),
    )

    fieldsets = (
        (None, {'fields': ('email', 'password', 'city')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_data_entry')})
    )


admin.site.register(Account, MyAdminAccounts)
