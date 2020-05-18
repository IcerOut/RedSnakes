from ConferenceManager import serializers
from ConferenceManager.models import Abstract, Bid, ConferenceAuthor, ConferenceAuthorSession, \
    ConferenceSession, Review
from RedSnakes.Service.MainService import MainService


class ReviewService(MainService):
    def __init__(self):
        super().__init__()

    def add(self, review):
        serializer = serializers.ReviewSerializer(data=review)
        if not serializer.is_valid():
            raise ValueError('Invalid JSON!')
        new_review = serializer.create(serializer.validated_data)
        Review.save(new_review)

    def update(self, entity):
        pass

    def getAll(self):
        reviews = Review.objects.all().order_by('paperId')
        reviews_json = serializers.ReviewSerializer(reviews, many=True)
        return reviews_json

    def get_by_id(self, review_id: int):
        review = Review.objects.get(pk=review_id)
        review_json = serializers.ReviewSerializer(review)
        return review_json

    def delete(self, entity):
        pass

    def add_bid(self, bid):
        serializer = serializers.BidSerializer(data=bid)
        if not serializer.is_valid():
            raise ValueError('Invalid JSON!')
        new_review = serializer.create(serializer.validated_data)
        Bid.save(new_review)

    def add_section(self, section, papers):
        serializer_section = serializers.ConferenceSessionSerializer(data=section)
        serializer_papers = serializers.PaperSerializer(data=papers, many=True)
        if not serializer_section.is_valid() or not serializer_papers.is_valid():
            raise ValueError('Invalid JSON!')
        new_section = serializer_section.create(serializer_section.validated_data)
        ConferenceSession.save(new_section)

        papers_list = []
        for paper in serializer_papers.validated_data:
            papers_list.append(serializer_papers.create(paper))

        authors_list = []
        for paper in papers_list:
            abstract = Abstract.objects.get(pk=paper.paperId)
            author = ConferenceAuthor.objects.get(pk=abstract.authorId)
            authors_list.append(author)

        for author in authors_list:
            conf_auth_session = ConferenceAuthorSession()
            conf_auth_session.conferenceAuthorId = author.pk
            conf_auth_session.conferenceSessionId = new_section.pk
            ConferenceAuthorSession.save(conf_auth_session)
