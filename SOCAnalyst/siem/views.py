from rest_framework.viewsets import ModelViewSet
from .models import SecurityEvent, Alert, Incident
from .serializers import SecurityEventSerializer, AlertSerializer, IncidentSerializer


class SecurityEventViewSet(ModelViewSet):
    queryset = SecurityEvent.objects.all()
    serializer_class = SecurityEventSerializer


class AlertViewSet(ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class IncidentViewSet(ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
