from django import forms
from .models import infoUser
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username',  'email', 'password')


class infoUserForm(forms.ModelForm):
    class Meta():
        model = infoUser
        fields = ('name', 'profile_picture')
