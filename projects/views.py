from django.http import HttpResponse
from django.shortcuts import render

from projects.models import SchoolGrade, VolunteerHours


# HttpResponse = response to what you requested on the page after request
# Create your views here.

def project_list(request):
    return render(request, 'home/index.html')
    # return HttpResponse('Hello World!')


def all_grades(request, year):
    year_dict = {"freshman": 'Year 9', "junior": 'Year 11'}
    y = year_dict[year]
    volunteers = VolunteerHours.objects.filter(year=y)
    grades = SchoolGrade.objects.filter(year=y)
    print(grades)
    return render(request, "home/year.html", {'grades': grades, 'volunteers': volunteers})

