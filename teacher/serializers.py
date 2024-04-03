from rest_framework import serializers
from . import models

class teacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    user = serializers.StringRelatedField(many=False)

    teaching_area = serializers.StringRelatedField(many=True)
    designation = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Teacher
        fields = '__all__'
        
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'
        
class teachingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.teachingArea
        fields = '__all__'
        
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(many=False)
    teacher = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = models.Review
        fields = '__all__'