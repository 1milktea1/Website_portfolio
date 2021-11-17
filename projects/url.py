from django.urls import path
from projects import views

app_name = 'home'

urlpatterns = [
    path('<str:year>', views.all_grades, name='all_grades'),
    path('index', views.project_list)]

