from django.db import models
from student.models import Student
from teacher.models import Teacher, AvailableTime
# Create your models here.

Class_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
Class_TYPES = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]
class DemoClass(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    class_types = models.CharField(choices = Class_TYPES, max_length = 10)
    class_status = models.CharField(choices = Class_STATUS, max_length = 10, default = "Pending")
    Subject = models.TextField()
    time = models.OneToOneField(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Teacher : {self.teacher.user.first_name} , Student : {self.student.user.first_name}"