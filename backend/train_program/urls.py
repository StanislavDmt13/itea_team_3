from django.urls import path
from . import views

urlpatterns = [
        path('', views.ProgramsView.as_view(), name='train-program-homepage'),

]