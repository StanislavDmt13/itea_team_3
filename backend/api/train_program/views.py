from rest_framework import generics
from db.models import Task, Category
from .serializers import TaskSerializer


class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
