from django.db import models

class SecurityEvent(models.Model):
    event_type = models.CharField(max_length=255)
    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} from {self.source_ip} to {self.destination_ip}"


class Alert(models.Model):
    SEVERITY_CHOICES = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
    STATUS_CHOICES = [('new', 'New'), ('investigating', 'Investigating'), ('resolved', 'Resolved')]

    event = models.ForeignKey(SecurityEvent, related_name="alerts", on_delete=models.CASCADE)
    severity = models.CharField(max_length=50, choices=SEVERITY_CHOICES)
    alert_message = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alert: {self.alert_message} - {self.severity} status: {self.status}"


class Incident(models.Model):
    STATUS_CHOICES = [('open', 'Open'), ('closed', 'Closed')]

    alert = models.ForeignKey(Alert, related_name="incidents", on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Incident: {self.description} status: {self.status}"
