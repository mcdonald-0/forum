from unicodedata import name
from django.urls import path

from questions.views import *

app_name = 'questions'
urlpatterns = [
    path('', HomePageView, name='home'),
]