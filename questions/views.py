from urllib import request
from django.http import HttpResponse 

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import render, redirect

from django.urls import reverse

from helpers.decorators import *

from questions.filters import *
from questions.models import *
from questions.forms import *

from authentication.models import *


def HomePageView(request, *args, **kwargs):
    tags = Tag.objects.all()
    questions = Question.objects.all()
    users = User.objects.all()
    userprofiles = UserProfile.objects.all()
    
    # ToDo: I need to download a homepage template because i have no idea currently on what to do

    context = {
        'tags': tags, 
        'questions': questions,
        'users': users,
        'profile': userprofiles,
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
            
            if request.user.userprofile.first_name == None:
                messages.warning(request, 'You need to create a profile before you can do that😣!')
                return redirect(f'/user/{ request.user.pk }/edit/?next={ request.path }')
            
            Answer.objects.create(question=question, answerer=request.user.userprofile, **form.cleaned_data)

            return redirect('questions:question', question_id=question_id, slug=slug)

    context = {
        'question': question,
        'answers_count': question.answers.count(),
        'now': timezone.now(),
        'form': form
    }
    return render(request, 'questions/question_view.html', context)


@login_required(login_url='authentication:signin')
def AskQuestion(request, *args, **kwargs):

    if request.user.userprofile.first_name == None:
        messages.warning(request, 'You need to create a profile before you can do that😣!')
        return redirect(f'/user/{ request.user.pk }/edit/?next={ request.path }')

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

def SearchResults(request, *args, **kwargs):

    if len(request.GET.get('x')) == 0:
        return HttpResponse('<h1>You did nnt input a search value😒</h1>')
    else:
        pass
   
   
    if request.method == 'GET':
        query = request.GET.get('x')
        search_results = Q(
            Q(title__istartswith=query) |
            Q(title__icontains=query) |  
            Q(tag__name__iexact=query) |
            Q(questioner__first_name__iexact=query) | 
            Q(questioner__user__username__exact=query)
            )

        results = Question.objects.filter(search_results)

    
    context = {
		'questions': results,
	}

    return render(request, 'questions/search_results.html', context)






    