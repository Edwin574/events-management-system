from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email',
                    'first_name', 'last_name', 'is_active']
    list_filter = ['is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']


admin.site.register(User, CustomUserAdmin)
