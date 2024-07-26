from django.contrib import admin
from .models import  Bank, GradingSystem, Grade, FailCriteria, Institute, FeeParticulars, Rules


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



@admin.register(GradingSystem)
class GradingSystemAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [GradeInLine]



@admin.register(FailCriteria)
class FailCriteriaAdmin(admin.ModelAdmin):
    list_display = ["id", "gradingSystem", "overAllPercentage", "subjectAllPercentage", "noSubject"]


@admin.register(FeeParticulars)
class FeeParticularsAdmin(admin.ModelAdmin):
    list_display = ["id", "prefixAmount", "label", "fee_class"]
    


@admin.register(Rules)
class RulesFeeParticularsAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    