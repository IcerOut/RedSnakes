from django.db import models


# Create your models here.
class Organization(models.Model):
    OrganizationID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)

    def __str__(self):
        return Organization

