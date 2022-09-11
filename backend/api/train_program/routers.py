from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'tasks', views.TaskAPIViewSet)
router.register(r'categories', views.CategoryAPIViewSet)