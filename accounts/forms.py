from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(ModelForm):
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order = ['username', 'password', 'password_check', 'email']

    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username', 'password', 'password_check', 'email']

class SignInForm(ModelForm):
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username', 'password']