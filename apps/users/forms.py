from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from apps.users.models import CustomUser


class UserCreateFrom(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'display_name', 'avatar')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'display_name', 'avatar')


class AvatarForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']
