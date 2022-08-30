from rest_framework.routers import DefaultRouter
from django.urls import path
# from .views import WorkoutAPIView
from .views import WorkoutViewSet

router = DefaultRouter()
router.register(r'workout', WorkoutViewSet, basename='user')

urlpatterns = router.urls




"""
# Django API используя Django Rest Framework

app_name = "workouts"

urlpatterns = [
    # Viewsets Django REST Framework
    path('workout/', WorkoutView.as_view({'get': 'list'})),
    path('workout/<int:pk>', WorkoutView.as_view({'get': 'retrieve'})),
]
    
"""