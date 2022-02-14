from django.urls import path

from users.views import *

app_name = 'users'
urlpatterns = [ 
    path('<user_id>/', UserProfileView, name='signup'),
]