from multiprocessing import context
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from users.forms import *
from users.models import *
from authentication.models import *

@login_required(login_url='authentication:signin')
def EditUserProfile(request, *args, **kwargs):
    # Modify this function that if someone wants to edit a profile that is not theirs, it redirects them to their profile
    # Also modify the frontend
    user_id = kwargs['user_id']
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponse('Something went wrong😥')
    if user.pk != request.user.pk:
        return HttpResponse('you cannot edit another profile😠')

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
