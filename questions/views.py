from django.http import HttpResponse

from django.shortcuts import render

from questions.models import *


def HomePageView(request):
    tags = Tag.objects.all()
    questions = Question.objects.all()

    # ToDo: I need to download a homepage template because i have no idea currently on what to do

    context = {
        'tags': tags,
        'questions': questions
    }
    return render(request, 'questions/index.html', context)








    