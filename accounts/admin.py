# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)
