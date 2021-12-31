from django.contrib import admin
from .models import (
    SchoolGrade,
    VolunteerHours,
    Highlights,
    HighlightImage,
    HighlightVideo,
)

# Register your models here.
tables = [SchoolGrade, VolunteerHours, Highlights, HighlightImage, HighlightVideo]
admin.site.register(tables)
