from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.TeacherViewset) # router er antena
router.register('teachingarea', views.teachingAreaViewset) # router er antena
router.register('available_time', views.AvailableTimeViewset) # router er antena
router.register('designation', views.DesignationViewset) # router er antena
router.register('reviews', views.ReviewViewset) # router er antena

urlpatterns = [
    path('', include(router.urls)),
]