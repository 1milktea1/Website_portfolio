from django.db import models


# Create your models here.
class SchoolGrade(models.Model):
    year = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    description = models.TextField()
    highlights = models.TextField(blank=True, null=True)


class VolunteerHours(models.Model):
    name = models.CharField(max_length=100)  # textfield doesnt have limit but char does
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    year = models.CharField(max_length=20)
    image = models.CharField(max_length=100)


class Highlights(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)


class HighlightImage(models.Model):
    image = models.CharField(max_length=100)
    highlight = models.ForeignKey(Highlights, on_delete=models.CASCADE)


class HighlightVideo(models.Model):
    video = models.TextField(max_length=100)
    highlight = models.ForeignKey(Highlights, on_delete=models.CASCADE)
