from django.http import HttpResponse 

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django import urls

from helpers.decorators import *

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
            return redirect('questions:question', question_id=question_id, slug=slug)

    #ToDo: I need to modify the view so that if a user just sign's up, he needs to create a userprofile before he answers a question so the answer does'nt shows his name as "None None"!

    context = {
        'question': question,
        'answers_count': question.answers.count(),
        'form': form
    }
    return render(request, 'questions/question_view.html', context)

@redirect_unregistered_user_to_signup
@user_with_no_userprofile
def AskQuestion(request, *args, **kwargs):

    #ToDo: I need to modify the user_with_no_userprofile decorator so that it has a next function so from here, they don't get redirected to view profile rather they get redirected back here

    form = AskQuestionForm()

    if request.method == 'POST':
        form = AskQuestionForm(request.POST)

        try:
            question = Question.objects.get(question=form.data['question'], title=form.data['title'], questioner=request.user.userprofile)
            if question:
                messages.error(request, f'You have already asked this question🤨')
            return redirect('questions:question', slug=question.slug, question_id=question.pk)

        except Question.DoesNotExist:
            if form.is_valid():
                question = Question.objects.create(questioner=request.user.userprofile, **form.cleaned_data)
            return redirect('questions:question', question.pk, question.slug)

    context = {
        'form': form,
    }

    return render(request, 'questions/ask_question.html', context)








    