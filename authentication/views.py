from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

from django.http import HttpResponse

from authentication.models import *
from authentication.forms import *
from users.models import *

def SignUpView(request, *args, **kwargs):

	form = SignUpForm()

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(**form.cleaned_data)
			userprofile = UserProfile.objects.create(user=user)

			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = authenticate(email=email, password=password)
			if user:
				login(request, user)

			return redirect('authentication:signin')
	
	context = {
		'form': form
	}
	return render(request, 'authentication/signup.html', context)

def SignInView(request, *args, **kwargs):

	form = SignInForm()

	if request.method == "POST":

		form = SignInForm(request.POST)
		if form.is_valid():

			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
				return HttpResponse(f'<h1>Hello {user.username}</h1>')
			else:
				message = 'Incorrect Username or Password!'
				form = SignInForm()

	context = {
		'form': form
	}
	return render(request, 'authentication/signin.html', context)
