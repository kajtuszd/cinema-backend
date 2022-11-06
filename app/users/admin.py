from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'username', 'is_moderator', 'email', 'phone', 'date_joined',)
    search_fields = ('first_name', 'last_name', 'username', 'email', 'phone',)
    list_filter = ('is_moderator',)
    ordering = ('first_name', 'last_name', 'username', 'email', 'date_joined',)


admin.site.register(User, UserAdmin)
