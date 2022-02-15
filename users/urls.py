from django.urls import path

from users.views import *

app_name = 'users'
urlpatterns = [ 
    path('<user_id>/', UserProfileView, name='view_profile'),
    path('<user_id>/edit/', EditUserProfile, name='edit_profile'),
]