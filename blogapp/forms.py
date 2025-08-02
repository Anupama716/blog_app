from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from blogapp.models import Blog



class RegistrationForm(UserCreationForm):

    class Meta:

        model=User

        fields= ["username","email","password1","password2"]

class SignInForm(forms.Form):

    username = forms.CharField()

    password=forms.CharField()

class BlogForm(forms.ModelForm):

    class Meta:

        model= Blog

        exclude=("created_at","owner") 