from django.urls import path
from . import views

urlpatterns = [
        path('category/<slug:cat_slug>/', views.TaskByCategoryView.as_view(), name='train-category'),
        path('task/<slug:task_slug>/', views.TaskDetailView.as_view(), name='train-task'),
        path('train/', views.CreateTrain.as_view(), name='train-train_program'),

]