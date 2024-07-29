from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
# from django.db.models import Q
from .models import eClass
from django.views.generic import DeleteView
from django.views.generic import CreateView, UpdateView
from django.http import JsonResponse

from django.views import View
from .forms import eClassForm
from teacher.models import Teacher

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



class eClassView(View):
    template_name = 'eClass/all_classes.html'

    def get(self, request):
        class_list = []
        try:
            classes = eClass.objects.filter(user = request.user)
            for cls in classes:

                class_list.append({
                    'id':cls.id,
                    'name': cls.name,
                    'boys': cls.boys_count(),
                    'girls': cls.girls_count(),
                    'total': cls.total_count(),

                })
        except:
            classes = None

        context = {'classes':class_list}

        return render(request, self.template_name, context)

         

class eClassUpdateView(View):
    template_name = 'eClass/create_class.html'

    def get(self, request, pk):
        try:
            eclass = get_object_or_404(eClass, pk = pk)
            if eclass.user != request.user:
                eclass = None

        except:
            eclass = None

        try:
            teachers = Teacher.objects.all()
            teachers_list = list(teachers.values_list('id', 'name'))
        except Teacher.DoesNotExist:
            teachers_list = None

        context = {'object': eclass}
        context['teachers'] = teachers_list
        return render(request, self.template_name, context)
        


    def post(self, request, pk):
        print("post reached")
        try:
            print("try reached")
            eclass = get_object_or_404(eClass, pk = pk)
            if not (eclass.user == request.user):
                eclass = None

        except:
            print("excapt reached")

            eclass = None
            
        print(eclass)    
        form = eClassForm(request.POST, instance=eclass)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('eClass:classes'))
        else:
            context = {'form': form}
            return render(request, self.template_name, context)





class eClassCreateView(CreateView):
    model = eClass
    form_class = eClassForm
    template_name = 'eClass/create_class.html'
    success_url = reverse_lazy('eClass:classes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            teachers = Teacher.objects.all()
            teachers_list = list(teachers.values_list('id', 'name'))
        except Teacher.DoesNotExist:
            teachers_list = None


        context['teachers'] = teachers_list
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user        
        obj.save()
        return super().form_valid(form)

    
# class eClassUpdateView(UpdateView):
#     model = eClass
#     form_class = eClassForm
#     template_name = 'eClass/create_class.html'
#     success_url = reverse_lazy('eClass:classes')

    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             teachers = Teacher.objects.all()
#             teachers_list = list(teachers.values_list('id', 'name'))
#         except Teacher.DoesNotExist:
#             teachers_list = None

#         context['teachers'] = teachers_list
#         return context




class eClassDeleteView(DeleteView):
    model = eClass
    template_name = 'eClass/all_classes.html'
    success_url = reverse_lazy('eClass:classes')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user == request.user:
            return super().delete(request, *args, **kwargs)
