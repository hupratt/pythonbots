# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser#, Profile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','id','last_login','is_superuser','first_name','last_name','is_staff','is_active','date_joined','bio','profile_pic']



admin.site.register(CustomUser, CustomUserAdmin)



