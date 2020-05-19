from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
# Register your models here.

from .models import *

# Register your models here.
class ExamAdmin(ModelAdmin):
    list_display = ["Question", "corrans","marks"]
    search_fields = ["Question"]
    list_filter = ["Question"]

admin.site.register(Exam, ExamAdmin)


class StudentProfileAdmin(ModelAdmin):
    list_display = ["Class","roll_No", "name"]
    search_fields = ["Class","roll_No", "name"]
    list_filter = ["Class"]

admin.site.register(StudentProfile, StudentProfileAdmin)