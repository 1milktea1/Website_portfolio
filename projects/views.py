from django.http import HttpResponse
from django.shortcuts import render

from projects.models import SchoolGrade


# HttpResponse = response to what you requested on the page after request
# Create your views here.

def project_list(request):
    return render(request, 'projects/index.html')
    # return HttpResponse('Hello World!')


def all_grades(request):
    grades = SchoolGrade.objects.all()
    return render(request, "projects/year.html", {'grades': grades})
