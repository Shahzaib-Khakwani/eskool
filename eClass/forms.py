from django import forms

from .models import eClass


class eClassForm(forms.ModelForm):
    class Meta:
        model = eClass
        fields = ['name', 'monthlyFee', 'teacher']