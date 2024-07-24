from django import forms
from .models import Institute


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ('name', 'logo', 'target_line', 'phone_number', 'website_url', 'address', 'country')
        
        
        
        