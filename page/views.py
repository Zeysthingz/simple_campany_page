from django.shortcuts import render
from random import randint


# from django.http import HttpResponse


# Create your views here.

def index(request):
    # print(request.META)
    # print(request.HEADER)
    # return HttpResponse("Hello, world. You're at the polls index.")

    return render(request, 'page/index.html',
                  {'hello': f"Hello, world. You\'re at the polls index {randint(0, 1000)}."})
