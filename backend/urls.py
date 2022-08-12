from django.urls import path, include


urlpatterns = [
    path('events/', include('backend.events.urls')),
    path('myprofile/', include('backend.myprofile.urls')),


    ]