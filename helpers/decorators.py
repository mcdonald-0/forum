from django.contrib import messages

from django.shortcuts import redirect

from django.http import HttpResponse



def already_signed_in_user(view_func):
	def wrapper(request, *args, **kwargs):
        
		if request.user.is_authenticated:
			return HttpResponse('<h1>You are already logged in</h1>')
			#ToDo: I need to modify this function so it redirects the user back to where they came from rather than displaying this static message.
		else:
			return view_func(request, *args, **kwargs)

	return wrapper

def redirect_unregistered_user_to_signup(view_func):
	def wrapper(request, *args, **kwargs):

		if not request.user.is_authenticated:
			messages.warning(request, 'You need to Sign In to perform that Action🥱!')
			return redirect('authentication:signin')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper

def user_with_no_userprofile(view_func):
	def wrapper(request, *args, **kwargs):
        
		if request.user.userprofile.first_name == None:
			messages.warning(request, 'You need to create a profile before you do that😣!')
			return redirect('users:edit_profile', user_id=request.user.pk)
		else:
			return view_func(request, *args, **kwargs)
            
	return wrapper





