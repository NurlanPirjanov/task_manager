from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *
from django.contrib.auth.models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','first_name','last_name','role_user',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar','role_user',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('last_name', 'first_name','avatar','role_user',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(RoleUser)