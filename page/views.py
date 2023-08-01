from django.shortcuts import render
from random import randint


# from django.http import HttpResponse


# Create your views here.

def index(request):
    # print(request.META)
    # print(request.HEADER)
    # return HttpResponse("Hello, world. You're at the polls index.")
    context={}

    return render(request, 'page/index.html',context)
