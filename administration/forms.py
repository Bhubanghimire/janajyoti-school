
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ( 'email', 'password')



class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields=('email','password')