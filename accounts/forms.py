
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']