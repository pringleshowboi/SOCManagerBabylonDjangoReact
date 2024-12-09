from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Case(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]
    
    # Case fields
    name = models.CharField(max_length=200)
    description = models.TextField()
    threat = models.ForeignKey('Threat', on_delete=models.CASCADE)  # Link to a threat
    assigned_analyst = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Case assigned to an analyst
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)  # Optional, filled when resolved
    
    def __str__(self):
        return f"Case: {self.name} - Status: {self.status}"
    
class Endpoint(models.Model):
    STATUS_CHOICES = [
        ('SECURE', 'Secure'),
        ('COMPROMISED', 'Compromised'),
        ('ISOLATED', 'Isolated'),
    ]
    
    # Endpoint fields
    name = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SECURE')
    last_seen = models.DateTimeField(auto_now=True)
    actions_taken = models.TextField(blank=True, null=True)  # Log of actions taken on the endpoint

    def __str__(self):
        return f"Endpoint: {self.name} - Status: {self.status}"
    
class Threat(models.Model):
    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    STATUS_CHOICES = [
        ('DETECTED', 'Detected'),
        ('RESOLVED', 'Resolved'),
        ('IN_PROGRESS', 'In Progress'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DETECTED')
    date_reported = models.DateTimeField(auto_now_add=True)
    actions_taken = models.TextField(blank=True, null=True)  # Actions taken in response to the threat

    def __str__(self):
        return f"Threat: {self.name} - Severity: {self.severity}"
        