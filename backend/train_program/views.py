from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView
from db.models import Task, Category


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'programs/task.html', {'task': task})


def show_category(request, cat_id):
    task_list = Task.objects.filter(category=cat_id)
    return render(request, 'programs/task_list.html', {'task_list': task_list})


class CategoriesView(ListView):
    model = Category
    context_object_name = 'categories'
