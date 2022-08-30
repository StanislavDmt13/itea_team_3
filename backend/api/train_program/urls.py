from django.urls import path, include
from .views import TaskAPIView

urlpatterns = [
    path('task_list/', TaskAPIView.as_view()),
    ]