from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate


import pycountry
from timezone_field import TimeZoneFormField

from .models import Institute, FeeParticulars,AccountSettings, Bank, Rules, GradingSystem, Grade, FailCriteria
from eClass.models import eClass
from student.models import Student
from .forms import InstituteForm, BankForm, RulesForm, AccountSettingsForm

from django.http import HttpResponse

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "myapp/index.html"



class CreateUpdateInstituteView(View):
    template_name = "myapp/institute_profile.html"

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
                'logo': None,
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
    template_name = "myapp/feeParticulars.html"

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




class BankView(View):
    template_name = "myapp/bank_profile.html"


    def get(self, request, pk=None):
        try:
            banks = Bank.objects.filter(user=request.user)
        except:
            banks = None

        paginator = Paginator(banks, 2)
        page = request.GET.get('page')

        try:
            banks_list = paginator.page(page)
        except PageNotAnInteger:
            banks_list = paginator.page(1)
        except EmptyPage:
            banks_list = paginator.page(paginator.num_pages)


        if pk:
            bank = get_object_or_404(Bank , pk = pk)
            context = {'bank':bank,'banks':banks_list, 'paginator_obj': banks_list}
        else:
            context = {'bank':None, 'banks':banks_list, 'paginator_obj': banks_list}
        
        return render(request, self.template_name, context)
    

    def post(self,request, pk = None):
        if pk:
            bank = get_object_or_404(Bank , pk = pk)
            form = BankForm(request.POST, request.FILES, instance=bank)
            if form.is_valid():
                form.save()
                return redirect(reverse_lazy('myapp:banks'))

            else:
                context  = {'form':form}
                return render(request, self.template_name, context)

        else:
            form = BankForm(request.POST, request.FILES)
            if form.is_valid():
                bank = form.save(commit=False)
                bank.user = request.user
                bank.save()

                return redirect(reverse_lazy('myapp:banks'))

            else:
                context  = {'form':form}

                return render(request, self.template_name, context)


def delete_bank(request, pk):
    bank = get_object_or_404(Bank, pk=pk)
    # if request.method == "POST":
    bank.delete()
        # return redirect('myapp:banks')
    return redirect('myapp:banks')




class RulesView(View):

    template_name = 'myapp/rules_form.html'

    def get(self, request):

        try:
            rules = get_object_or_404(Rules, user = request.user)
        except:
            rules = None

        context = {"rules": rules}

        return render(request, self.template_name, context)
    


    def post(self, request, pk=None):
        form = RulesForm(request.POST)

        if pk:
            try:
                rules = get_object_or_404(Rules, pk = pk)
                form = RulesForm(request.POST, instance=rules)
            except:
                form = RulesForm(request.POST)
        else:
            form = RulesForm(request.POST)


        if form.is_valid():
            rules = form.save(commit=False)
            rules.user = request.user
            rules.save()

            context = {'form':None}
        else:
            context = {'form':form}

        return render(request, self.template_name, context)



class GradingView(View):
    template_name = 'myapp/grading.html'

    def get(self, request):
        try:
            grading_system = get_object_or_404(GradingSystem, user = request.user)
        except:
            grading_system = None

        context = {'grading_system': grading_system}

        return render(request, self.template_name, context)
    
    def post(self, request):
        marks_bol = request.POST.get('marks')
        fail_bol = request.POST.get('fail')
        

        


        # print(grades)
        # print(to_values)
        # print(from_values)
        # print(status_values)
        # print(nosubjects)
        # print(percentage)
        # print(marks_bol)
        # print(fail_bol )
        # print(type(overall))

        try:
            grading_system = GradingSystem.objects.create(user = request.user)
        except:
            grading_system = get_object_or_404(GradingSystem, user = request.user)
            grading_system.grades.all().delete()

        if marks_bol == 'marks':
            grades = request.POST.getlist('grade')
            from_values = request.POST.getlist('from')
            to_values = request.POST.getlist('to')
            status_values = request.POST.getlist('status')
            for grade, from_value, to_value, status in zip(grades, from_values, to_values, status_values):
                if grade.strip() and from_value.strip() and to_value.strip() and status.strip():
                    grade = Grade.objects.create(gradingSystem = grading_system, grade = grade, fromPercentage = from_value, toPercentage = to_value, status = status)
        else:
            overall = request.POST.get('overall')
            percentage = request.POST.get('percentage')
            nosubjects = request.POST.get('nosubjects')
            if overall.strip() or (percentage.strip() and nosubjects.strip()) :
                try:
                    overall = int(overall)
                except:
                    overall = None
                
                try:
                    percentage = int(percentage)
                except:
                    percentage = None

                try:
                    nosubjects = int(nosubjects)
                except:
                    nosubjects = None


                try:
                    fail_creteria = get_object_or_404(FailCriteria, gradingSystem = grading_system)
                    fail_creteria.overAllPercentage = overall
                    fail_creteria.subjectAllPercentage = percentage
                    fail_creteria.noSubject = nosubjects
                    fail_creteria.save()
                except:
                    
                    fail_creteria = FailCriteria.objects.create(gradingSystem = grading_system, overAllPercentage = overall, subjectAllPercentage = percentage, noSubject = nosubjects)

       


        return redirect(reverse_lazy("myapp:grading"))


class AccountSettingsView(View):
    template_name = 'myapp/account_settings.html' 


    def get(self, request):
        try:
            account_setting = get_object_or_404(AccountSettings, user = request.user)
        except:
            account_setting = None

        timezone = TimeZoneFormField()
        context = {'countries':pycountry.countries, 'timezone': timezone.choices , 'account_settings':account_setting}

        return render(request, self.template_name, context)

    def post(self, request):
        timezone = request.POST.get('timezone')
        country = request.POST.get('country')
        currency = request.POST.get('currency')

        # print(timezone)
        # print(country)
        # print(currency)


        try:
            account_setting = get_object_or_404(AccountSettings, user = request.user)
        except:
            account_setting = AccountSettings.objects.create(user = request.user)

        form = AccountSettingsForm(request.POST, instance=account_setting)

        if form.is_valid():
            obj = form.save(commit=False)
            if timezone:
                obj.timezone = timezone
            if currency:
                obj.currency = currency


        account_setting.save()

        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

    
        user = authenticate(request, username=username, password=password1)

        if user is not None and account_setting.user == user:
            account_setting.user.set_password(password2)




        return redirect(reverse_lazy("myapp:account"))