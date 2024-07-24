from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Institute, FeeParticulars
from eClass.models import eClass
from student.models import Student
from .forms import InstituteForm

from django.http import HttpResponse
# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"



class CreateUpdateInstituteView(View):
    template_name = "institute_profile.html"

    def get(self, request):
        institute = get_object_or_404(Institute, user=request.user)
        if institute:
            print(institute)
            context = {
                'name': institute.name,
                'logo': institute.logo,
                'target_line': institute.target_line,
                'phone_number': institute.phone_number,
                'website_url': institute.website_url,
                'address': institute.address,
                'country': institute.country,
            }
            return render(request, self.template_name, {"context":context})
        else:

            context = {
                'name': None,
                'target_line':None,
                'logo': institute.logo,
                'phone_number': None,
                'website_url': None,
                'address': None,
            }
            print(context)
            return render(request, self.template_name, context)


    

    def post(self, request):
        form = InstituteForm(request.POST, request.FILES)
        if form.is_valid():
            institute = form.save(commit=False)
            institute.user = request.user
            institute.save()
        else:
            context = {'form': form}
            return render(request, self.template_name, context)



class feeParticularsView(View):
    template_name = "feeParticulars.html"

    def get(self, request):
        return render(request, self.template_name)


    

    def post(self, request):
        labels = request.POST.getlist('label')  
        prefixAmounts = request.POST.getlist('prefixAmount')
        fee_class = request.POST.get("fee_class")
        student = request.POST.get("students")
        if fee_class is not None:
            eclass = get_object_or_404(eClass, id=fee_class)
            for label, amount in zip(labels, prefixAmounts):
                if label.strip() and amount.strip():
                    try:
                        amount = int(amount)  
                        feeParticular = FeeParticulars.objects.create(label=label, prefixAmount = amount, fee_class = eclass)
                    except ValueError:
                        continue
                    

        elif student is not None:
            studenttoput = get_object_or_404(Student, id=student)
            for label, amount in zip(labels, prefixAmounts):
                if label.strip() and amount.strip():
                    try:
                        amount = int(amount)  
                        feeParticular = FeeParticulars.objects.create(label=label, prefixAmount = amount)
                        feeParticular.students.add(studenttoput)
                    except ValueError:
                        continue
                    

        else:
            studentstoPut = Student.objects.all()
            for label, amount in zip(labels, prefixAmounts):
                if label.strip() and amount.strip():
                    try:
                        amount = int(amount)  
                        feeParticular = FeeParticulars.objects.create(label=label, prefixAmount = amount)
                        feeParticular.students.set(studentstoPut)
                    except ValueError:
                        continue

                    


        print(labels)
        print(prefixAmounts)
        print(fee_class)
        print(student)

        return HttpResponse({
            'student':fee_class,
            'CLASS':student
        })

