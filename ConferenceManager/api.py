from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ConferenceManager import serializers
from ConferenceManager.models import Conference
from RedSnakes.Service.ConferenceService import ConferenceService
from RedSnakes.Service.ReviewService import ReviewService
from ConferenceManager.models import Conference, ConferenceAuthor, Participant


def conference_list(request):
    if request.method == 'GET':
        conferences = Conference.objects.all()
        conferences_json = serializers.ConferenceSerializer(conferences, many=True)
        return JsonResponse(conferences_json.data, safe=False)
    return HttpResponse(status=405)


def add_new_conference(request):
    if request.method == 'POST':
        service = ConferenceService()
        service.add(request.body.decode('utf-8'))
        return HttpResponse(status=200)
    return HttpResponse(status=405)

def get_conference_by_id(request):
    if request.method == 'GET':
        conference_id = request.GET.get('id')
        service = ConferenceService()
        conference = service.get_by_id(conference_id)
        return JsonResponse(conference.data)
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


