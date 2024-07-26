from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'myapp'

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    # path("institute-profile/", views.InstituteProfileView.as_view(), name='instituteProfile'), 

    path("create-institute-profile/", views.CreateUpdateInstituteView.as_view(), name='createInstituteProfile'), 

    path("fee-particulars/", views.feeParticularsView.as_view(), name='feeParticulars'), 

    path("banks/", views.BankView.as_view(), name='banks'), 
    path("banks/<int:pk>/delete", views.delete_bank, name='deleteBank'), 
    path("banks/<int:pk>/update", views.BankView.as_view(), name='updateBank'),

    path("rules/", views.RulesView.as_view(), name='rules'), 


  

]