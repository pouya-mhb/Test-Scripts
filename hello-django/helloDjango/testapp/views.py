from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def app (request):
    return HttpResponse ('hello')


def app2 (request):
      return HttpResponse ('hello app2')


    # c = a + b 
    
    # index = {
    #     'SUM' : c
    # }

    # return render (request,index,sum.html)


def app3 (request):
    return HttpResponse ('hello app3')

def app4 (request):
    return HttpResponse ('hello app4')