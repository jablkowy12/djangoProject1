from rest_framework import routers
from django.urls import include, path
from .views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
