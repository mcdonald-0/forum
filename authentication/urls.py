from django.urls import path

from authentication.views import *

app_name = 'authentication'
urlpatterns = [ 
    path('signup/', SignUpView, name='signup'),
    path('signin/', SignInView, name='signin'),
] 