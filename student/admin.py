from django.contrib import admin

# Register your models here.
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "registration", "studentClass", "discountPercentage"]
    list_filter = ["studentClass", "discountPercentage", "prevSchoolName", "religion", "bloodGroup", "orphanStatus"]
