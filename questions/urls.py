from unicodedata import name
from django.urls import path

from questions.views import *

app_name = 'questions'
urlpatterns = [
    path('', HomePageView, name='home'),
    path('<int:question_id>/<slug:slug>/', QuestionView, name='question'),
    path('ask/', AskQuestion, name='ask'),
]