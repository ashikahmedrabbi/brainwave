from django.contrib import admin

# Register your models here.
from .models import Teacher, teachingArea, professionalExperience, AvailableTime, Review

admin.site.register(Teacher)
admin.site.register(teachingArea)
admin.site.register(professionalExperience)
admin.site.register(AvailableTime)
admin.site.register(Review)

