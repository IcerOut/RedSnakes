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
    locationX = models.FloatField()
    locationY = models.FloatField()
    photoURL = models.CharField(max_length=255)
    street = models.CharField(max_length=255)


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

    def lofOut(self):
        """
         Log out
        """
        pass


    def __str__(self):
        return f'User[FullName = {self.fullName} ]'

    __repr__ = __str__



class Conference(models.Model):
    """
    Stores the information about a Conference
    Fields:
        -category: Varchar(50)
        -coordsX: float
        -coordsY: float
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
    coordsX = models.FloatField()
    coordsY = models.FloatField()
    deadlineAbstract = models.DateField()
    deadlineBiding = models.DateField()
    deadlinePaper = models.DateField()
    deadlineReview = models.DateField()
    descriprion = models.TextField()
    email = models.EmailField()
    startDate = models.DateField()
    endDate = models.DateField()
    ownerEmail = models.DateField()
    price = models.FloatField()
    researchTopics = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    def __str__(self):
        return f'Conference[Title = {self.title} ]'

    __repr__ = __str__


class ConferenceCategory(models.Model):
    """
        Stores the information about a ConferenceCategory
        Fields:
            title: varchar(200)
            conference = FK of Concerence
    """
    title = models.CharField(max_length=200)
    conference = models.ForeignKey(Conference, on_delete=models.PROTECT)


    def __str__(self):
        return f'ConferenceCategory[Title = {self.title} , Conference = {self.conference} ]'