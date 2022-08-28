from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView
from db.models import Task, Category


class TaskDetailView(DetailView):
    model = Task
    template_name = 'programs/task.html'
    slug_url_kwarg = 'task_slug'
    context_object_name = 'task'


class TaskByCategoryView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'programs/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(category__slug=self.kwargs['cat_slug'])


class CategoriesView(ListView):
    model = Category
    context_object_name = 'categories'
