import traceback

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ConferenceManager import serializers
from ConferenceManager.models import Conference, ConferenceAuthor, Participant
from RedSnakes.Service.ConferenceService import ConferenceService
from RedSnakes.Service.PapersService import PapersService
from RedSnakes.Service.ReviewService import ReviewService

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def conference_list(request):
    if request.method == 'GET':
        conferences = Conference.objects.all()
        conferences_json = serializers.ConferenceSerializer(conferences, many=True)
        return JsonResponse(conferences_json.data, safe=False)
    return HttpResponse(status=405)


def add_new_conference(request):
    response_data = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        submissionDeadline = request.POST.get('submissionDeadline')
        reviewDeadline = request.POST.get('reviewDeadline')
        conferenceDate = request.POST.get('conferenceDate')

        response_data = {'name': name, 'submissionDeadline': submissionDeadline,
                         'reviewDeadline': reviewDeadline, 'conferenceDate': conferenceDate}

        Conference.objects.create(
            name=name,
            submissionDeadline=submissionDeadline,
            reviewDeadline=reviewDeadline,
            conferenceDate=conferenceDate
        )
        return JsonResponse(response_data)
    return HttpResponse(status=405)


def sign_up(request):
    if request.metho == 'POST':
        conference_id = request.POST.get('conference_id')
        conference = Conference.objects.get(pk=conference_id)
        participant_id = request.POST.get('participant_id')
        participant = Participant.objects.get(pk=participant_id)
        service = ConferenceService()
        service.signUp(participant, conference)
        HttpResponse(status=200)
    return HttpResponse(status=405)


@csrf_exempt
def add_new_review(request: HttpRequest):
    if request.method == 'POST':
        try:
            ReviewService().add(request.body.decode('utf-8'))
            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def get_all_reviews(request: HttpRequest):
    if request.method == 'GET':
        try:
            reviews = ReviewService().getAll()
            return JsonResponse(reviews.data, safe=False)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def add_new_bid(request: HttpRequest):
    if request.method == 'POST':
        try:
            ReviewService().add_bid(request.body.decode('utf-8'))
            return HttpResponse(status=200)
        except Exception as e:
            traceback.print_exc()
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def get_all_sections(request: HttpRequest):
    if request.method == 'GET':
        try:
            reviews = ConferenceService().get_all_sections()
            return JsonResponse(reviews.data, safe=False)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def add_section(request: HttpRequest):
    if request.method == 'POST':
        try:
            ConferenceService().add_section(request.body.decode('utf-8'))
            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


def get_conference_by_id(request):
    if request.method == 'GET':
        conference_id = request.GET.get('id')
        conference = Conference.objects.get(pk=conference_id)
        conference_json = serializers.ConferenceSerializer(data=conference)
        return JsonResponse(conference_json, safe=False)
    return HttpResponse(status=405)


def sign_up(request):
    if request.method == 'POST':
        conference_id = request.POST.get('conference_id')
        conference = Conference.objects.get(pk=conference_id)
        participant_id = request.POST.get('participant_id')
        participant = Participant.objects.get(pk=participant_id)
        ConferenceAuthor.objects.create(
            pEmail=participant.email,
            cId=conference.pk
        )
        response_data = {
            'pEmail': participant.email,
            'cId': conference_id
        }
        return JsonResponse(response_data)
    return HttpResponse(status=405)


def find_paper(request):
    if request.method == 'GET':
        try:
            paper_id = request.GET.get('id')
            paper = Conference.objects.get(pk=paper_id)
            paper_json = serializers.PaperSerializer(data=paper)
            return JsonResponse(paper_json, safe=False)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def get_all_papers(request: HttpRequest):
    if request.method == 'GET':
        try:
            paperService = PapersService()
            papers = paperService.getAll()
            return JsonResponse(papers.data, safe=False)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def get_all_papers_not_in_sections(request: HttpRequest):
    if request.method == 'GET':
        try:
            paperService = PapersService()
            papers = paperService.getAllNotInSections()
            return JsonResponse(papers.data, safe=False)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def add_new_paper(request: HttpRequest):
    if request.method == 'POST':
        try:
            paperService = PapersService()
            paperService.add(request.body.decode('utf-8'))
            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def add_new_abstract(request: HttpRequest):
    if request.method == 'POST':
        try:
            paperService = PapersService()
            abstract = paperService.sendAbstract(request.body.decode('utf-8'))
            paperService.add(abstract)
            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def file_upload(request: HttpRequest):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['mile']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'speaker-register.html', context)


@csrf_exempt
def send_reviewer(request):
    if request.method == 'POST':
        try:
            paperService = PapersService()
            paperService.assignReviewer(request.body.decode('utf-8'))
            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def get_reviewers(request):
    if request.method == 'GET':
        try:
            abstract = request.GET.get('abstract_id')
            paperService = PapersService()
            bids = paperService.getBidsForOnePaper(abstract)
            return JsonResponse(bids.data, safe=False)
        except Exception as e:
            return HttpResponse(e, status=400)
    else:
        return HttpResponse(status=405)
