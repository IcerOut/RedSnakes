import json
from datetime import date, datetime

from ConferenceManager import serializers
from ConferenceManager.models import Abstract, Conference, ConferenceAuthor, \
    ConferenceAuthorSession, ConferenceSession, \
    Paper, Participant, ProgramCommitteeMember
from RedSnakes.Service.MainService import MainService


class ConferenceService(MainService):
    def __init__(self):
        super().__init__()

    def add(self, entity):
        conference_serializer = serializers.ConferenceSerializer(data=entity)
        if not conference_serializer.is_valid():
            raise ValueError("Invalid JSON")
        new_conference = conference_serializer.create(conference_serializer.validated_data)
        Conference.save(new_conference)

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

    def signUp(self, participant, conference):
        conference_serializer = serializers.Conference(data=conference)
        participant_serializer = serializers.Participant(data=participant)

        if not participant_serializer.is_valid() or not conference_serializer.is_valid():
            raise ValueError("Invalid JSON")

        cid = conference.pk
        email = participant.email
        author = ConferenceAuthor(pEmail=email, cId=cid)

        conference_author_serializer = serializers.ConferenceAuthor(data=author)
        ConferenceAuthor.save(author)

        return conference_author_serializer

    def get_by_id(self, conference_id: int):
        conference = Conference.objects.get(pk=conference_id)
        conference_serializer = serializers.ConferenceSerializer(conference)
        return conference_serializer

    def getAll(self):
        conferences = Conference.objects.all().order_by('name')
        conferences_serializer = serializers.ConferenceSerializer(conferences, many=True)
        return conferences_serializer

    def get_all_sections(self):
        sections = ConferenceSession.objects.all().order_by('date')
        sections_json = serializers.ConferenceSessionSerializer(sections, many=True)
        return sections_json

    def add_section(self, section_json):
        section = json.loads(section_json)
        title = section['title']
        chair_name = section['chairName']
        chair = Participant.objects.get(name=chair_name)
        pcId = ProgramCommitteeMember.objects.get(pEmail=chair)
        newSession = ConferenceSession(title=title, pcId=pcId, date=date.today(),
                                       startHour=datetime.now(), endHour=datetime.now(),
                                       roomNumber='999')  # FIXME
        newSession.save()
        for paper_id in section['idPapers']:
            abstract_id = Paper.objects.get(id=paper_id).id
            authorId = Abstract.objects.get(id=abstract_id).id
            newConferenceAuthorSession = ConferenceAuthorSession(
                conferenceAuthorId=ConferenceAuthor.objects.get(id=authorId),
                conferenceSessionId=newSession)
            newConferenceAuthorSession.save()
