from django.shortcuts import redirect

from django.http import HttpResponse

from .models import *


def unregistered_user(view_func):
	def wrapper(request, *args, **kwargs):
        
		if request.user.is_authenticated:
			return HttpResponse('<h1>You are logged in</h1>')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper