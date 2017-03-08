from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.

def home(request):
    ''' show recent 5 questions '''
    return HttpResponse("home")

def ask(request, user_id):
    return HttpResponse("you are %s." % user_id)

def reply(request, question_id, user_id):
    return HttpResponse('qusiton id %s and user_id %s .' % (question_id,user_id))

def detail(request, question_id):
    return HttpResponse('Detail of question %s .' % question_id)
