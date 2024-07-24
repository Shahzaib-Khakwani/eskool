from django.urls import path
from . import views

app_name = 'eClass'

urlpatterns = [
    path("search-class", views.classSearchListView, name='searchClass'),
]