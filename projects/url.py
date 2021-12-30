from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('<str:year>', views.all_grades, name='all_grades'),
    path('', views.home_page)
]


Others_url = 'http://yumeng-zou-highschool.herokuapp.com/others'