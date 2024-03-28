from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

from lost_and_found.objects_posts.models import Post, Object
from django import forms

from lost_and_found.utils.mixins import InputStyleMixin


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('object', 'found')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('object',)


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"

class LoginForm(AuthenticationForm):
    pass


class CreateUserForm(InputStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


