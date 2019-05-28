# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

from .models import CustomUser#, Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class SubForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'profile_pic',
        ]


class SubForm2(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username'
        ]
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = [
#             'profile_pic'
#         ]

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    # profile_pic = forms.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'profile_pic')