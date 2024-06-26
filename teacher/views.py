from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

class teachingAreaViewset(viewsets.ModelViewSet):
    queryset = models.teachingArea.objects.all()
    serializer_class = serializers.teachingAreaSerializer
    
    
class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    

class AvailableTimeForSpecificTeacher(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        teacher_id = request.query_params.get("teacher_id")
        if teacher_id:
            return query_set.filter(teacher = teacher_id)
        return query_set

class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificTeacher]

class TeacherPagination(pagination.PageNumberPagination):
    page_size = 6 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class TeacherViewset(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.teacherSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = TeacherPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'teaching_area__name']
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer