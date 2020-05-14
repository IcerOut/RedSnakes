from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from ConferenceManager.models import *


def add_new_conference(request):
    conferences = Conference.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        submissionDeadline = request.POST.get('submissionDeadline')
        reviewDeadline = request.POST.get('reviewDeadline')
        conferenceDate = request.POST.get('conferenceDate')

        response_data['name'] = name
        response_data['submissionDeadline'] = submissionDeadline
        response_data['reviewDeadline'] = reviewDeadline
        response_data['conferenceDate'] = conferenceDate

        Conference.objects.create(
            name = name,
            submissionDeadline = submissionDeadline,
            reviewDeadline = reviewDeadline,
            conferenceDate = conferenceDate
            )
        return JsonResponse(response_data)

    return render(request, 'submit-new-conference.html', {'conferences':conferences})

def home(request):
    return render(request, "home.html")

def conference_list(request):
    return render(request, "conference-list.html")

def evaluation_results(request):
    return render(request, "evaluation-results.html")

# def submit_new_conference(request):
#     return render(request, "submit-new-conference.html")

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
    return render(request, "split-papers-into-sections.html")
