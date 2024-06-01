from django.shortcuts import render
from django.http import HttpResponse

def custom(request):
    return HttpResponse("Hello world!")
