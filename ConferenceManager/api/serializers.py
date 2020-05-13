from rest_framework import serializers

from ..models import Author, Paper

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'affiliation', 'email', 'title', 'conference', 'section')


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    # Necessary for the many-to-many relation
    author = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Paper
        fields = ('name', 'noPages', 'paperKind', 'evalDecision', 'conference', 'author')
