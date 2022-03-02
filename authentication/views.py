from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

from django.http import HttpResponse

from authentication.models import *
from authentication.forms import *

from helpers.decorators import *

from users.models import *

@already_signed_in_user
def SignUpView(request, *args, **kwargs):

	form = SignUpForm()

	if request.method == 'POST':

		form = SignUpForm(request.POST)

		if form.is_valid():

			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = User.objects.create_user(username=username, email=email, password=password)
			
			UserProfile.objects.create(user=user, pk=user.pk)

			user = request.POST['username']
			messages.success(request, 'An account was created for ' + user)

			return redirect('authentication:signin')
	
	context = {
		'form': form,
	}
	return render(request, 'authentication/signup.html', context)

@already_signed_in_user
def SignInView(request, *args, **kwargs):

	form = SignInForm()

	if request.method == "POST":

		form = SignInForm(request.POST)

		if form.is_valid():

			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = authenticate(email=email, password=password)

			login(request, user)
			return HttpResponse('Success!')
		
	context = {
		'form': form
	}
	return render(request, 'authentication/signin.html', context)

#? 320 square meters by 320 square meters 4 bedroom with four bq en`suite

#! Fix the bug that keeps user in the login screen even after getting logged in, this happens after login_required() has been called. It is supposed to log them in and then return them to the url they were before but it still keeps them in the login screen with the url http://127.0.0.1:8000/signin/?next=/user/1/. 


