from ConferenceManager import serializers
from ConferenceManager.models import Conference
from RedSnakes.Service.MainService import MainService


class ConferenceService(MainService):
    def __init__(self):
        super().__init__()

    def signUp(self, entity):
        conference_serializer = serializers.ConferenceSerializer(data=entity)
        if not conference_serializer.is_valid():
            raise ValueError("Invalid JSON")
        new_conference = conference_serializer.create(conference_serializer.validated_data)
        Conference.save(new_conference)

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

    def get_by_id(self, conference_id: int):
        conference = Conference.objects.get(pk=conference_id)
        conference_json = serializers.ConferenceSerializer(conference)
        return conference_json

    def getAll(self):
        conferences = Conference.objects.all().order_by('name')
        conferences_json = serializers.ConferenceSerializer(conferences, many=True)
        return conferences_json

