from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path("search-student/", views.studentSearchListView, name="searchStudent"),
]