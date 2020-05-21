import json

from ConferenceManager import serializers
from ConferenceManager.models import Paper, Abstract
from RedSnakes.Service.MainService import MainService


class PapersService(MainService):
    def __init__(self):
        super().__init__()

    def add(self, entity):
        paper = json.loads(entity)
        serializer = serializers.PaperSerializer(data=paper)
        if not serializer.is_valid():
            raise ValueError('Invalid JSON!', serializer.errors)
        new_paper = serializer.create(serializer.validated_data)
        Paper.save(new_paper)

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

    def getAll(self):
        papers = Paper.objects.all().order_by('paperId')
        papers_json = serializers.PaperSerializer(papers, many=True)
        return papers_json

    def getById(self, paper_id: int):
        paper = Paper.objects.get(pk=paper_id)
        paper_json = serializers.PaperSerializer(paper)
        return paper_json

    def sendAbstract(self, abstract_json):
        abstract_json = json.loads(abstract_json)
        serializer = serializers.AbstractSerializer(data=abstract_json)
        if not serializer.is_valid():
            raise ValueError('Invalid JSON!', serializer.errors)
        abstract = serializer.create(serializer.validated_data)
        Abstract.save(abstract)
        return abstract
