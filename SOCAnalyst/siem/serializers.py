from rest_framework import serializers
from .models import SecurityEvent, Alert, Incident


class SecurityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityEvent
        fields = '__all__'


class AlertSerializer(serializers.ModelSerializer):
    event = SecurityEventSerializer(read_only=True)  # Include event details if needed

    class Meta:
        model = Alert
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    alert = AlertSerializer(read_only=True)  # Include alert details if needed

    class Meta:
        model = Incident
        fields = '__all__'
