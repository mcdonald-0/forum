from django.contrib import messages
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME

from django.shortcuts import render, redirect

from django.http import HttpResponse

from authentication.models import *
from authentication.forms import *
from users.models import *

def SignUpView(request, *args, **kwargs):

	if request.method == 'POST':

		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		# Fix this code so that the form validates the input and checks the database if there is a user with that email or username. 

		user = User.objects.create_user(username=username, email=email, password=password)
		UserProfile.objects.create(user=user)

		user = form.cleaned_data.get('username')
		messages.success(request, 'An account was created for ' + user)

		return redirect('authentication:signin')
	
	context = {
		'form': form
	}
	return render(request, 'authentication/signup.html', context)

def SignInView(request, *args, **kwargs):

	if request.method == "POST":

		email = request.POST['email']
		password = request.POST['password']

		user = authenticate(email=email, password=password)
		if user:
			login(request, user)
		else:
			messages.info(request, 'Username OR Password is incorrect!')

	context = {}
	return render(request, 'authentication/signin.html', context)


def get_redirect_url(self):
	"""Return the user-originating redirect URL if it's safe."""
	redirect_to = self.request.POST.get(
		self.redirect_field_name,
		self.request.GET.get(self.redirect_field_name, '')
	)
	url_is_safe = url_has_allowed_host_and_scheme(
		url=redirect_to,
		allowed_hosts=self.get_success_url_allowed_hosts(),
		require_https=self.request.is_secure(),
	)
	return redirect_to if url_is_safe else ''


# Fix the bug that keeps user in the login screen even after getting logged in, this happens after login_required() has been called. It is supposed to log them in and then return them to the url they were before but it still keeps them in the login screen with the url http://127.0.0.1:8000/signin/?next=/user/1/. 


