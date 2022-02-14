from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from users.forms import *
from users.models import *
from authentication.models import *

@login_required(login_url='authentication:signin')
def UserProfileView(request, *args, **kwargs):

    user_id = kwargs['user_id']
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponse('Something went wrong😥')
    if user.pk != request.user.pk:
        return HttpResponse('you cannot edit another profile😠')

    form = UserProfileForm()

    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    # if request.method == 'POST':
        
    #     form = UserProfileForm(request.POST, request.FILES, instance=user)
        
    #     if form.is_valid():
    #         try:
    #             user = user.userprofile
    #         except user.DoesNotExist:
    #             form.save()
    #         # up = UserProfile.objects.update_or_create(**form.cleaned_data)
    #         # up.save()

    #         print(form.cleaned_data)
    #         print(user.userprofile)
    #         return HttpResponse('<h1>Success</h1>')

    context = {
        'form': form
    }
    return render(request, 'users/view_profile.html', context)
