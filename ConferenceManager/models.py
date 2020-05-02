from django.db import models


# Create your models here.
class Organization(models.Model):
    """
    Stores the information about an Organization
    Fields:
        Title - Varchar(255)
    """
    # OrganizationID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'Organization[Title={self.title}]'

    __repr__ = __str__


class User(models.Model):
    """
    Stores the information about an User
    Fields:
        Organization - FK
        UserCategory - Varchar(255)
        Affiliation - Varchar(255)
        Email - Varchar()
        FullName - Varchar(255)
        LocationX - float
        LocationY - float
        PhotoURL - varchar(255)
        Street - varchar(255)
    """
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    userCategory = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255)
    email = models.EmailField()
    fullName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    webPage = models.CharField(max_length=255)


    def createAccount(self):
        """
        Create an account
        """
        pass

    def logIn(self):
        """
        Log in into account
        """
        pass

    def logOut(self):
        """
         Log out
        """
        pass


    def __str__(self):
        return f'User[FullName = {self.fullName}]'

    __repr__ = __str__



class Conference(models.Model):
    """
    Stores the information about a Conference
    Fields:
        -category: Varchar(50)
        -deadlineAbstract: date
        -deadlineBiding: date
        -deadlinePaper: date
        -deadlineReview: date
        -descriprion: text
        -email: string
        -startDate: date
        -endDate: date
        -ownerEmail: string
        -price: float
        -researchTopics: string
        -title: Varchar(50)
        -website:Varchar(50)
    """
    category = models.CharField(max_length=50)
    deadlineAbstract = models.DateField()
    deadlineBiding = models.DateField()
    deadlinePaper = models.DateField()
    deadlineReview = models.DateField()
    description = models.TextField()
    email = models.EmailField()
    startDate = models.DateField()
    endDate = models.DateField()
    ownerEmail = models.DateField()
    price = models.FloatField()
    researchTopics = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    def __str__(self):
        return f'Conference[Title = {self.title}]'

    __repr__ = __str__


class ConferenceCategory(models.Model):
    """
        Stores the information about a ConferenceCategory
        Fields:
            title: varchar(255)
            conference = FK of Conference
    """
    title = models.CharField(max_length=255)
    conference = models.ForeignKey(Conference, on_delete=models.PROTECT)


    def __str__(self):
        return f'ConferenceCategory[Title = {self.title} , Conference = {self.conference}]'

    __repr__ = __str__


class ResearchTopic(models.Model):
    """
    Stores information about a ResearchTopic
    Fields:
        category: varchar(255)
        conferenceCategory: FK references ConferenceCategory
        name: varchar(255)
    """
    category = models.CharField(max_length=255)
    conferenceCategory = models.ForeignKey(ConferenceCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'ResearchTopic[Category = {self.category}, ConferenceCategory = {self.conferenceCategory}, Name = {self.name} ]'

    __repr__ = __str__


class Paper(models.Model):
    """
    Stores information about a Paper
    Fields:
        authorEmail: varchar(255)
        conference: FK references Conference
        conferenceName: varchar(255)
        fileURL: varchar(255)
        status: varchar(255)
        timestamp: varchar(255)
        abstract: varchar(10000)
        title: varchar(255)
    """
    authorEmail = models.EmailField()
    conference = models.ForeignKey(Conference, on_delete=models.PROTECT)
    conferenceName = models.CharField(max_length=255)
    fileURL = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=255)
    abstract = models.CharField(max_length=1000)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'Paper[AuthorEmail = {self.authorEmail}, conference = {self.conference}, , fileURL = {self.fileURL}, status = {self.status}, timestamp = {self.timestamp}, abstract = {self.abstract}, title = {self.title}]'

    __repr__ = __str__


class Review:
    """
    Stores information about a Review
    Fields:
        user: FK references User
        paper: FK references Paper
        assignedReviewerEmail: varchar(255)
        conferenceName: varchar(255)
        paperTitle: varchar(255)
        review: varchar(255)
        status: varchar(255)
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    paper = models.ForeignKey(Paper, on_delete=models.PROTECT)
    assignedReviewerEmail = models.CharField(max_length=255)
    conferenceName = models.CharField(max_length=255)
    paperTitle = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'Review[User = {self.user}, Paper = {self.paper}, AssignedReviewerEmail = {self.assignedReviewerEmail}, ConferenceName = {self.conferenceName}, Review = {self.review}, status = {self.status}]'

    __repr__ = __str__


class ChairMember(User):
    def evaluatePapers(self):
        pass
    def chooseSelectionParticipate(self):
        pass

class Speaker(User):
    def editPaper(self):
        pass
    def chooseSection(self):
        pass

class Listener(User):
    def enlistToConference(self):
        pass
    def chooseSection(self):
        pass

class ScMember(ChairMember):
    pass

class PcMember(ChairMember):
    def chooseReviewPaper(self):
        pass

class Chair(ChairMember):
    def askForExtraReview(self):
        pass
    def assignReviewPaper(self,paperId):
        pass
class CoChair(ChairMember):
    def assignReviewPaper(self,paperId):
        pass





