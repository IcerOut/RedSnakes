from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


def home(request):
    return render(request, "home.html")

def conference_list(request):
    return render(request, "conference-list.html")