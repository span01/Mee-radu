from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Customer,Comment

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','last_name','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','phone','address']