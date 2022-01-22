# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project

# Form for regsitering a new user
class RegisterForm(UserCreationForm):
    
    # Sign up form fields
    email = forms.EmailField(max_length=200, required=True)
    username = forms.CharField(max_length=50, required=True)
    password1 = forms.CharField(max_length=50, required=True)
    password2 = forms.CharField(max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', )

# Form for creating a new project
class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'tags', )
