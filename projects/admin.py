from django.contrib import admin
from .models import SchoolGrade, VolunteerHours

# Register your models here.
tables = [SchoolGrade, VolunteerHours]
admin.site.register(tables)
