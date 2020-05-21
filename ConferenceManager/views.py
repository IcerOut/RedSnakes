import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.models import User


# Create your views here.
from django.template import RequestContext

from ConferenceManager import serializers
from ConferenceManager.models import *

def user_list(request):
    users = User.objects.all()
    # form = request.POST
    # if request.method == 'POST':
    #     select_user = get_object_or_404(User, pk=request.POST.get('user_id'))
    #     # user.user = select_user
    #     user.save()

    # context = {
    #     "users": User.objects.all()
    # }
    return render(request, 'split-papers-into-sections.html', {'users':users})

def add_new_conference(request):
    conferences = Conference.objects.all()
    return render(request, 'submit-new-conference.html', {'conferences': conferences})


def home(request):
    return render(request, "home.html")


def conference_list(request):
    return render(request, "conference-list.html")


def chair_register(request):
    return render(request, "chair-register.html")

def speaker_register(request):
    return render(request, "speaker-register.html")

def listener_register(request):
    return render(request, "listener-register.html")

def evaluation_results(request):
    return render(request, "evaluation-results.html")

def assign_reviewers(request):
    return render(request, "assign-reviewers.html")


def bidding(request):
    return render(request, "bidding.html")


def evaluation(request):
    return render(request, "evaluation.html")


def review(request):
    return render(request, "review.html")


def section_choices(request):
    return render(request, "section-choices.html")


def split_papers_into_sections(request):
    users = User.objects.all()
    return render(request, "split-papers-into-sections.html", {'users':users})
