from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'home/index.html')


def About(request):
    return render(request, 'about/index.html')


def Contact(request):
    return render(request, 'contact/index.html')
