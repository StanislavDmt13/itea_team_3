from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyWorkout.as_view(), name='workout'),
    path('create_workout/', views.create_workout, name='create_workout'),
    path('<int:pk>/', views.detail_workout, name='detail_workout'),
    path('<int:pk>/update', views.WorkoutUpdatelView.as_view(), name='update_workout'),
    path('<int:pk>/delete', views.WorkoutDeletelView.as_view(), name='delete_workout'),

]
