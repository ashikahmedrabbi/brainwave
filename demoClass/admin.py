from django.contrib import admin
from . import models

class DemoClassAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'student_name', 'classTypes', 'classStatus', 'subject', 'time', 'cancel']
    
    def student_name(self, obj):
        return obj.student.user.first_name
    
    def teacher_name(self, obj):
        return obj.teacher.user.first_name
    
admin.site.register(models.DemoClass, DemoClassAdmin)
