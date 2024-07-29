from django.contrib import admin
from .models import  Bank,AccountSettings, GradingSystem, Grade, FailCriteria, Institute, FeeParticulars, Rules, GradingSystem, Grade, FailCriteria

from django.utils.html import format_html
# Register your models here.



@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ["id", "name" ,"user", "country"]
    list_filter = ["user", "country"]



@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ["id", "name" ,"address"]
    list_filter = ["user"]


class GradeInLine(admin.TabularInline):
    model = Grade
    raw_id_fields = ['gradingSystem']


class FailCriteriaInLine(admin.TabularInline):
    model = FailCriteria
    raw_id_fields = ['gradingSystem']



@admin.register(GradingSystem)
class GradingSystemAdmin(admin.ModelAdmin):
    def grade_list(self, obj):
        return format_html('<br>'.join([grade.grade for grade in obj.grades.all()]))

    grade_list.short_description = 'grades'
    list_display = ['id', 'user', 'grade_list']
    inlines = [GradeInLine, FailCriteriaInLine]



@admin.register(FailCriteria)
class FailCriteriaAdmin(admin.ModelAdmin):
    list_display = ["id", "gradingSystem", "overAllPercentage", "subjectAllPercentage", "noSubject"]


@admin.register(FeeParticulars)
class FeeParticularsAdmin(admin.ModelAdmin):
    list_display = ["id", "prefixAmount", "label", "fee_class"]
    


@admin.register(Rules)
class RulesFeeParticularsAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    

# @admin.register(GradingSystem)
# class GradingSystemAdmin(admin.ModelAdmin):

#     def grade_list(self, obj):
#         return format_html('<br>'.join([grade.grade for grade in obj.grades.all()]))

#     grade_list.short_description = 'grades'

#     list_display = ('name', )
#     list_display = ["id", "user", "grade_list"]
    


@admin.register(AccountSettings)
class AccountSettingsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "timezone", "country", "currency"]