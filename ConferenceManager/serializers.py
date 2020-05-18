from rest_framework import serializers

from .models import Abstract, Bid, Conference, Paper, ProgramCommitteeMember, Review


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


class AbstractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Abstract
        fields = ('authorId', 'text', 'title')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    pcId = ProgramCommitteeMemberSerializer()
    paperId = PaperSerializer()

    class Meta:
        model = Review
        fields = ('paperId', 'pcId', 'status')


class BidSerializer(serializers.HyperlinkedModelSerializer):
    abstractId = AbstractSerializer()
    pcId = ProgramCommitteeMemberSerializer()

    class Meta:
        model = Bid
        fields = ('abstractId', 'pcId', 'status')
