from django.views.generic import ListView, DetailView, CreateView
from db import models
from . import forms


class TaskDetailView(DetailView):
    model = models.Task
    template_name = 'programs/task.html'
    slug_url_kwarg = 'task_slug'
    context_object_name = 'task'


class TaskByCategoryView(ListView):
    model = models.Task
    context_object_name = 'task_list'
    template_name = 'programs/task_list.html'

    def get_queryset(self):
        return models.Task.objects.filter(category__slug=self.kwargs['cat_slug'])


class CategoriesView(ListView):
    model = models.Category
    context_object_name = 'categories'


class CreateTrain(CreateView):
    model = models.TrainProgram
    form_class = forms.TrainForm
    template_name = 'programs/train_program.html'
