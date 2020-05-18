from ConferenceManager import serializers
from ConferenceManager.models import Paper, Abstract
from RedSnakes.Service.MainService import MainService


class PapersService(MainService):
    def __init__(self):
        super().__init__()

    def add(self, entity):
        pass

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
        abstract = serializers.AbstractSerializer(abstract)
        return abstract
