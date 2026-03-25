from django.db import models

# Create your models here.
class IOC(models.Model):
    IOC_TYPES = [
        ("IP", "IP"),
        ("Domain", "Domain"),
        ("Hash", "Hash"),
        ("URL", "URL"),
    ]
    type = models.CharField(max_length=20, choices=IOC_TYPES)
    value = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value
    