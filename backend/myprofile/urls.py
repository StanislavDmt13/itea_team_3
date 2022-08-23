from django.urls import path
from . import views

urlpatterns = [

    path('edit/', views.ProfileEditView.as_view(), name='myprofile-edit'),
    path('', views.HomepageView.as_view(), name='myprofile-homepage'),
    path('edit/avatar/', views.change_avatar, name='myprofile-edit-avatar'),
]