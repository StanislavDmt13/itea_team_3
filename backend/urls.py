from django.urls import path, include


urlpatterns = [
    path('events/', include('backend.events.urls')),
    path('myprofile/', include('backend.myprofile.urls')),
    path('auth/', include('backend.authorization.urls')),
    path('auth/', include('django.contrib.auth.urls')),

    ]