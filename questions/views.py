from django.http import HttpResponse

from django.shortcuts import render, redirect

from questions.models import *
from questions.forms import *


def HomePageView(request, *args, **kwargs):
    tags = Tag.objects.all()
    questions = Question.objects.all()

    # ToDo: I need to download a homepage template because i have no idea currently on what to do

    context = {
        'tags': tags,
        'questions': questions
    }
    return render(request, 'questions/index.html', context)

def QuestionView(request, *args, **kwargs):

    slug = kwargs['slug']
    question_id = kwargs['question_id']
    try:
        question = Question.objects.get(slug=slug, pk=question_id)
    except Question.DoesNotExist:
        return HttpResponse('There is no such question')

    
    form = AnswerForm()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            Answer.objects.create(question=question, answerer=request.user.userprofile, **form.cleaned_data)
            return redirect('questions:question', slug=slug)


    context = {
        'question': question,
        'form': form
    }
    return render(request, 'questions/question_view.html', context)

def AskQuestion(request, *args, **kwargs):

    form = AskQuestionForm()
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.create(questioner=request.user.userprofile, **form.cleaned_data)
        return redirect('questions:question', question.pk, question.slug)

    context = {
        'form': form,
    }
    return render(request, 'questions/ask_question.html', context)








    