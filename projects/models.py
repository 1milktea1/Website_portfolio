from django.db import models


# Create your models here.
class SchoolGrade(models.Model):
    year = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    description = models.TextField()
    highlights = models.TextField(null=True)


class VolunteerHours(models.Model):
    name = models.CharField(max_length=100) #textfield doesnt have limit but char does
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    year = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
