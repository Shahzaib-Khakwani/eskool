from django import forms
from .models import Institute, Bank, Rules


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ('name', 'logo', 'target_line', 'phone_number', 'website_url', 'address', 'country')
        

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ('name', 'image', 'accountNumber', 'address', 'instructions')
        
        
        
class RulesForm(forms.ModelForm):
    class Meta:
        model = Rules
        fields = ['rules']