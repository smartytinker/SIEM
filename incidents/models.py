from django.db import models

# Create your models here.
class Incident(models.Model):
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    source = models.CharField(max_length=200, blank=True)
    host = models.CharField(max_length=200, blank=True)
    mitre_technique = models.CharField(max_length=50, blank=True)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title