from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World.  You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("Your're looking at question %s. " % question_id)

def results(request, question_id):
    response = "You're looking at the results of quesiton %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s. " question_id)



# Create your views here.