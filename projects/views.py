from django.http import HttpResponse
from django.shortcuts import render

from projects.models import SchoolGrade, VolunteerHours


# HttpResponse = response to what you requested on the page after request
# Create your views here.

# def project_list(request):
#     return render(request, 'projects/index.html')
#     # return HttpResponse('Hello World!')


def all_grades(request, year):
    year_dict = {
        "freshman": "Year 9",
        "sophomore": "Year 10",
        "junior": "Year 11",
        "senior": "Year 12"
    }

    y = year_dict[year]
    volunteers = VolunteerHours.objects.filter(year=y)
    grades = SchoolGrade.objects.filter(year=y)
    print(grades)
    return render(request, "projects/year.html", {'grades': grades, 'volunteers': volunteers})


def home_page(request):
    return render(request, 'projects/index.html')
