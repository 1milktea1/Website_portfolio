from django.urls import path
from projects import views

app_name = "projects"

urlpatterns = [
    path("highlights", views.highlights_page),
    path("<str:year>", views.all_grades, name="all_grades"),
    path("", views.home_page),
]
