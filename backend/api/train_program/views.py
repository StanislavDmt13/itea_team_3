from rest_framework import viewsets
from db.models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class TaskAPIViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

