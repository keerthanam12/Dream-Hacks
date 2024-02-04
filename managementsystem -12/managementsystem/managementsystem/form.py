from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.core.exceptions import ValidationError

class StudentUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@citchennai.net'):
            raise ValidationError('Email must end with @citchennai.net')
        return email