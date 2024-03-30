from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        user = serializers.StringRelatedField(many=False)
        model = models.Student
        fields = '__all__'