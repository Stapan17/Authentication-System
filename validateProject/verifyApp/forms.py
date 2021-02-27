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


class infoUserUpdateForm(forms.ModelForm):
    class Meta():
        model = infoUser
        fields = ("name", "profile_picture")

    def save(self, commit=True):
        info_user = self.instance
        info_user.name = self.cleaned_data['name']

        if self.cleaned_data['profile_picture']:
            info_user.profile_picture = self.cleaned_data['profile_picture']

        if commit:
            info_user.save()

        return info_user
