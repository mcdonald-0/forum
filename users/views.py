from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.contrib import messages

from authentication.models import *
from helpers.decorators import *
from users.forms import *
from users.models import *


@redirect_unauthenticated_user_to_signin(login_url='authentication:signin')
def EditUserProfile(request, *args, **kwargs):
    #Todo: Modify the frontend of this view
    user_id = kwargs['user_id']

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponse('Something went wrong😥')

    if user.pk != request.user.pk:
        messages.info(request, 'What are you doing😕')
        messages.info(request, 'Try editing your own profile😏')
        return redirect('users:edit_profile', user_id=request.user.pk)

    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user, pk=request.user.pk)
        profile.save()

    form = UserProfileForm(instance=request.user.userprofile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()

            destination = request.POST.get('next')
 
            if destination:
                return redirect (destination)

            return redirect('users:view_profile', user_id=request.user.pk)

    context = {
        'form': form
    }
    return render(request, 'users/edit_profile.html', context)

def UserProfileView(request, *args, **kwargs):
    user_id = kwargs['user_id']
    
    try:
        profile = UserProfile.objects.get(pk=user_id)
    except UserProfile.DoesNotExist:
        return HttpResponse('That user does not exist!')

    context = {
        'user': profile,
    }
    return render(request, 'users/view_profile.html', context)
