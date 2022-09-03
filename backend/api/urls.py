from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    )

urlpatterns = [
    path('myprofile/', include('backend.api.myprofile.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('programs/', include('backend.api.train_program.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]