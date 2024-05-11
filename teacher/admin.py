from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.AvailableTime)

class teachingAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }
    
admin.site.register(models.teachingArea, teachingAreaAdmin)
admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Teacher)
admin.site.register(models.Review)