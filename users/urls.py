from django.urls import path

from users.views import *

app_name = 'users'
urlpatterns = [ 
    path('<slug:slug>/<user_id>/', UserProfileView, name='view_profile'),
    path('<slug:slug>/<user_id>/edit/', EditUserProfile, name='edit_profile'),
]