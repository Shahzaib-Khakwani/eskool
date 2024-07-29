from django.urls import path
from . import views

app_name = 'eClass'

urlpatterns = [
    path("search-class", views.classSearchListView, name='searchClass'),
    path("all/", views.eClassView.as_view(), name='classes'),
    path("create/", views.eClassCreateView.as_view(), name='createClass'),
    path("update/<int:pk>/", views.eClassUpdateView.as_view(), name='updateClass'),
    path("delete/<int:pk>/", views.eClassDeleteView.as_view(), name='deleteClass'),
]