from rest_framework import serializers

from .models import Abstract, Bid, Conference, ConferenceAuthor, ConferenceAuthorSession, \
    ConferenceSession, Login, Paper, Participant, ProgramCommitteeMember, Review


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ('name', 'submissionDeadline', 'reviewDeadline', 'conferenceDate')

    def create(self, validated_data):
        conference = Conference()
        conference.name = validated_data['name']
        conference.submissionDeadline = validated_data['submissionDeadline']
        conference.reviewDeadline = validated_data['reviewDeadline']
        conference.conferenceDate = validated_data['conferenceDate']
        return conference


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('email', 'password')


class ParticipantSerializer(serializers.ModelSerializer):
    email = LoginSerializer()

    class Meta:
        model = Participant
        fields = ('email', 'name', 'website', 'affiliation')


class ConferenceAuthorSerializer(serializers.ModelSerializer):
    pEmail = ParticipantSerializer()

    class Meta:
        model = ConferenceAuthor
        fields = ('pEmail', 'cId', 'rank')


class AbstractSerializer(serializers.ModelSerializer):
    authorId = ConferenceAuthorSerializer()

    class Meta:
        model = Abstract
        fields = ('id', 'authorId', 'text', 'title')

    def create(self, validated_data):
        abstract = Abstract()
        abstract.authorId = validated_data['authorId']
        abstract.text = validated_data['text']
        abstract.title = validated_data['title']
        return abstract


class PaperSerializer(serializers.ModelSerializer):
    paperId = AbstractSerializer()

    class Meta:
        model = Paper
        fields = ('id', 'paperId', 'path', 'accepted')

    def create(self, validated_data):
        paper = Paper()
        paper.paperId = validated_data['paperId']
        paper.path = validated_data['path']
        paper.accepted = validated_data['accepted']
        return paper


class ProgramCommitteeMemberSerializer(serializers.ModelSerializer):
    pEmail = ParticipantSerializer()

    class Meta:
        model = ProgramCommitteeMember
        fields = ('id', 'pEmail', 'cId', 'rank')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('paperId', 'pcId', 'status', 'justification', 'recommendations')

    def create(self, validated_data):
        review = Review()
        review.paperId = validated_data['paperId']
        review.pcId = validated_data['pcId']
        review.status = validated_data['status']
        review.justification = validated_data['justification']
        review.recommendations = validated_data['recommendations']
        return review


class FullReviewSerializer(serializers.ModelSerializer):
    paperId = PaperSerializer()
    pcId = ProgramCommitteeMemberSerializer()

    class Meta:
        model = Review
        fields = ('paperId', 'pcId', 'status', 'justification', 'recommendations')

    def create(self, validated_data):
        review = Review()
        review.paperId = validated_data['paperId']
        review.pcId = validated_data['pcId']
        review.status = validated_data['status']
        review.justification = validated_data['justification']
        review.recommendations = validated_data['recommendations']
        return review


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('abstractId', 'pcId', 'status')

    def create(self, validated_data):
        bid = Bid()
        bid.abstractId = validated_data['abstractId']
        bid.pcId = validated_data['pcId']
        bid.status = validated_data['status']
        return bid


class FullBidSerializer(serializers.ModelSerializer):
    pcId = ProgramCommitteeMemberSerializer()

    class Meta:
        model = Bid
        fields = ('abstractId', 'pcId', 'status', 'chosenToReview')

    def create(self, validated_data):
        bid = Bid()
        bid.abstractId = validated_data['abstractId']
        bid.pcId = validated_data['pcId']
        bid.status = validated_data['status']
        bid.chosenToReview = validated_data['chosenToReview']
        return bid


class ConferenceSessionSerializer(serializers.ModelSerializer):
    pcId = ProgramCommitteeMemberSerializer()

    class Meta:
        model = ConferenceSession
        fields = ['id', 'title', 'pcId', 'date', 'startHour', 'endHour', 'roomNumber']

    def create(self, validated_data):
        sess = ConferenceSession()
        sess.pcId = validated_data['pcId']
        sess.date = validated_data['date']
        sess.startHour = validated_data['startHour']
        sess.endHour = validated_data['endHour']
        sess.roomNumber = validated_data['roomNumber']
        return sess


class ConferenceAuthorSessionSerializer(serializers.ModelSerializer):
    conferenceAuthorId = ConferenceAuthorSerializer()
    conferenceSessionId = ConferenceSessionSerializer()

    class Meta:
        model = ConferenceAuthorSession
        fields = ['conferenceAuthorId', 'conferenceSessionId']
