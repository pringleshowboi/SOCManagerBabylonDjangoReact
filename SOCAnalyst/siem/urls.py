from django.urls import path, include
from rest_framework.routers import DefaultRouter
from siem.views import SecurityEventViewSet, AlertViewSet, IncidentViewSet

router = DefaultRouter()
router.register(r'events', SecurityEventViewSet, basename='securityevent')
router.register(r'alerts', AlertViewSet, basename='alert')
router.register(r'incidents', IncidentViewSet, basename='incident')

urlpatterns = [
    path('api/', include(router.urls)),
]
