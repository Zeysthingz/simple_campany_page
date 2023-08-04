from django.urls import path, include
from .views import (
    index,
    about,
    contact,
    page_view,
)

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('<slug:slug>', page_view, name='pages'),
]
