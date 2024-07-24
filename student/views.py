from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Student
from django.db.models import Q
from django.http import JsonResponse



def studentSearchListView(request):
    if request.method == 'GET':
        query = request.GET.get("query")
        if query:
            object_list = Student.objects.filter(
            Q(name__icontains=query) | Q(registration__icontains=query)
        )
            results = list(object_list.values('id', 'name'))
        else:
            results = []
        return JsonResponse(results, safe=False)