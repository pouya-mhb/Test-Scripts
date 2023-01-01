from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app (request):
    return HttpResponse ('hello')


def app2 (request):
    return HttpResponse ('hello')


def app3 (request):
    return HttpResponse ('hello')

def app4 (request):
    return HttpResponse ('hello')