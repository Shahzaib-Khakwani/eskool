from django.shortcuts import render
# from django.db.models import Q
from .models import eClass
from django.views.generic import ListView
from django.http import JsonResponse

    
def classSearchListView(request):
    if request.method == 'GET':
        query = request.GET.get("query")
        if query:
            object_list = eClass.objects.filter(
                name__icontains=query
            )
            results = list(object_list.values('id', 'name'))
        else:
            results = []
        return JsonResponse(results, safe=False)

