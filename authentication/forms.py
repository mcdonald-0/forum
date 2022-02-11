from django import forms
from django.contrib.auth import authenticate

from authentication.models import *

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150, 
        label="", 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Username'
                }
            )
        )
    email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Email'
                }
            )
        )
    password = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password', 
                'class': 'form-control',
                'placeholder': 'Password'
                }
            )
        )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SignInForm(forms.ModelForm):
    email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Email'
                }
            )
        )
    password = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password', 
                'class': 'form-control',
                'placeholder': 'Password'
                }
            )
        )
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Incorrect Email or Password!')