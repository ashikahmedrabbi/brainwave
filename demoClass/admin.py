from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from . import models

class DemoClassAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'student_name', 'classTypes', 'classStatus', 'subject', 'time', 'cancel']
    
    def student_name(self, obj):
        return obj.student.user.first_name
    
    def teacher_name(self, obj):
        return obj.teacher.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_types == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_email.html', {'user' : obj.student.user, 'teacher' : obj.teacher})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.student.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
 
    
admin.site.register(models.DemoClass, DemoClassAdmin)
