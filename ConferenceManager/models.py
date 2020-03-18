from django.db import models


# Create your models here.
class Organization(models.Model):
    """
    Stores the information about an Organization
    Fields:
        OrganizationID - PK, AutoIncrement
        Title - Varchar(255)
    """
    OrganizationID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)

    def __str__(self):
        return f'Organization[OrganizationID={self.OrganizationID}, Title={self.Title}]'

    __repr__ = __str__
