from django.shortcuts import render

from django.http import HttpResponse

from authentication.models import *

def home(request):
    return HttpResponse(f'<h1>Hello</h1>')
