from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'first_name', 'last_name', 'cpf', 'is_provider', 'is_staff']
    list_filter = ['is_provider', 'is_staff', 'is_superuser', 'groups']
    search_fields = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_provider', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        # Remove 'date_joined' from this fieldset
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_provider', 'is_staff')}
        ),
    )


admin.site.register(User, UserAdmin)
