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
