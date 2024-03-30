from rest_framework import serializers
from . import models

class DemoClasstSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False)
    student = serializers.StringRelatedField(many=False)
    teacher = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.DemoClass
        fields = '__all__'