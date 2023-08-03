from django.shortcuts import render



# from django.http import HttpResponse


# Create your views here.

def index(request):
    # print(request.META)
    # print(request.HEADER)
    # return HttpResponse("Hello, world. You're at the polls index.")
    page_title = "Home"
    context = {
        "page_title": page_title,
    }
    print(context)
    return render(request, 'page/index.html', context)


def about(request):
    page_title="About"
    context = {
        "page_title": page_title,
    }
    return render(request, 'page/about.html', context)

def contact(request):
    page_title="Contact"
    hero_title = "Contact Us!"
    hero_text= "We are here to help you"
    context = {
        "page_title": page_title,
        "hero_title": hero_title,
        "hero_text": hero_text,
    }
    return render(request, 'page/contact.html', context)
