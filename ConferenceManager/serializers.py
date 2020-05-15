from rest_framework import serializers

from .models import Conference


class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conference
        fields = ('name', 'submissionDeadline', 'reviewDeadline', 'conferenceDate')
