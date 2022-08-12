from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<str:month>/', views.event_calendar, name='events_calendar'),
    ]