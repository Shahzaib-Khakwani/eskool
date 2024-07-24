from django.contrib import admin

# Register your models here.
from .models import eClass

class eClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'monthlyFee')
    # list_filter = ('monthly_tution_fee', 'institute__institute_name', 'Select_Class_Teacher')

admin.site.register(eClass, eClassAdmin)