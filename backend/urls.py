from django.urls import path, include

# from backend.apiworkout.views import WorkoutAPIView

urlpatterns = [
    path('events/', include('backend.events.urls')),
    path('myprofile/', include('backend.myprofile.urls')),
    path('auth/', include('backend.authorization.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('workout/', include('backend.workout.urls')),
    path('apiw/', include('backend.apiworkout.urls')),

    ]
