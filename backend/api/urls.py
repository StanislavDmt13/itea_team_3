from django.urls import path, include


urlpatterns = [
    path('myprofile/', include('backend.api.myprofile.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('programs/', include('backend.train_program.urls')),

    ]