from django.urls import path, include


urlpatterns = [
    path('events/', include('backend.events.urls')),
    path('', include('backend.myprofile.urls')),
    path('auth/', include('backend.authorization.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('programs/', include('backend.train_program.urls')),
    path('workout/', include('backend.workout.urls')),
    path('api/', include('backend.api.urls')),
    path('apiw/', include('backend.apiworkout.urls')),

    ]