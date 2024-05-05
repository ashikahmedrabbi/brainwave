from django.contrib import admin

from .models import DemoClass

admin.site.register(DemoClass)

# Register your models here.
from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class DemoClassAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'student_name', 'class_types', 'class_status', 'Subject', 'time', 'cancel']
    def student_name(self,obj):
        return obj.student.user.first_name
    
    def teacher_name(self,obj):
        return obj.teacher.user.first_name
    
    
    
admin.site.register(models.DemoClass, DemoClassAdmin)