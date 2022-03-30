from django.urls import path

from users.views import *

app_name = 'users'
urlpatterns = [ 
    path('<user_id>/<slug:slug>/', UserProfileView, name='view_profile'),
    path('<user_id>/<slug:slug>/edit/', EditUserProfile, name='edit_profile'),
]