from django.http import HttpResponse, JsonResponse
from ConferenceManager import serializers
from ConferenceManager.models import Conference

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
