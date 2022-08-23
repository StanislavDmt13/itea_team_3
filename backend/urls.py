from django.urls import path, include
from backend.myprofile import views

urlpatterns = [
    path('events/', include('backend.events.urls')),
    path('myprofile/', include('backend.myprofile.urls')),
    path('auth/', include('backend.authorization.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('programs/', include('backend.train_program.urls')),
    path('', views.HomepageView.as_view(), name='myprofile-homepage'),
    ]