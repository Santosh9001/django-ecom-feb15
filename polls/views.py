from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is index method view")

def detail(request,question_id):
    return HttpResponse("Related question %s", question_id)

def results(request,question_id):
    response = "You are looking at the result of %s"
    return HttpResponse(response % question_id)