from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import (
    UserAttributeSimilarityValidator, 
    CommonPasswordValidator, 
    NumericPasswordValidator
)

from authentication.models import *

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150, 
        label="Username", 
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
        min_length=6,
        max_length=128,
        validators={
            UserAttributeSimilarityValidator,  
        },
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password', 
                'class': 'form-control',
                'placeholder': 'Password'
                }
            )
        )
        #ToDo: I need to add password validators to the signup form.
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
            try:
                check_email = User.objects.get(email=email)
                if check_email:
                    raise forms.ValidationError(f'Incorrect password for email "{check_email}"😓')

            except User.DoesNotExist:
                raise forms.ValidationError('You do not have an account yet😕, try creating one🙂!')
           