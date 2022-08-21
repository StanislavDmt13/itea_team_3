from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_workout, name='workout'),
    path('create_workout/', views.create_workout, name='create_workout'),
]
