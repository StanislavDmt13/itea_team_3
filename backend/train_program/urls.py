from django.urls import path
from . import views

urlpatterns = [
        path('category/<int:cat_id>/', views.show_category, name='train-category'),
        path('task/<int:pk>/', views.task_detail, name='train-task'),

]