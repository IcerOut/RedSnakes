from rest_framework import serializers

from .models import Abstract, Bid, Conference, ConferenceAuthor, ConferenceAuthorSession, \
    ConferenceSession, Login, Paper, Participant, ProgramCommitteeMember, Review


class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conference
        fields = ('name', 'submissionDeadline', 'reviewDeadline', 'conferenceDate')


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper
        fields = ('paperId', 'path', 'accepted')


class ProgramCommitteeMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgramCommitteeMember
        fields = ('pEmail', 'cId', 'rank')


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ('email', 'password')


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    email = LoginSerializer()

    class Meta:
        model = Participant
        fields = ('email', 'name', 'website', 'affiliation')


class ConferenceAuthorSerializer(serializers.HyperlinkedModelSerializer):
    pEmail = ParticipantSerializer()

    class Meta:
        model = ConferenceAuthor
        fields = ('pEmail', 'cId', 'rank')


class AbstractSerializer(serializers.HyperlinkedModelSerializer):
    authorId = ConferenceAuthorSerializer()

    class Meta:
        model = Abstract
        fields = ('authorId', 'text', 'title')

    def create(self, validated_data):
        abstract = Abstract()
        abstract.authorId = validated_data['authorId']
        abstract.text = validated_data['text']
        abstract.title = validated_data['title']
        return abstract


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    pcId = ProgramCommitteeMemberSerializer()
    paperId = PaperSerializer()

    class Meta:
        model = Review
        fields = ('paperId', 'pcId', 'status')

    def create(self, validated_data):
        review = Review()
        review.paperId = validated_data['paperId']
        review.pcId = validated_data['pcId']
        review.status = validated_data['status']
        return review


class BidSerializer(serializers.HyperlinkedModelSerializer):
    abstractId = AbstractSerializer()
    pcId = ProgramCommitteeMemberSerializer()

    class Meta:
        model = Bid
        fields = ('abstractId', 'pcId', 'status')

    def create(self, validated_data):
        bid = Bid()
        bid.abstractId = validated_data['abstractId']
        bid.pcId = validated_data['pcId']
        bid.status = validated_data['status']
        return bid


class ConferenceSessionSerializer(serializers.HyperlinkedModelSerializer):
    pcId = ProgramCommitteeMemberSerializer()

    class Meta:
        model = ConferenceSession
        fields = ['pcId', 'date', 'startHour', 'endHour', 'roomNumber']


class ConferenceAuthorSessionSerializer(serializers.HyperlinkedModelSerializer):
    conferenceAuthorId = ConferenceAuthorSerializer()
    conferenceSessionId = ConferenceSessionSerializer()

    class Meta:
        model = ConferenceAuthorSession
        fields = ['conferenceAuthorId', 'conferenceSessionId']
