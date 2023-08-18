from django.db import models
from fcm_django.models import FCMDevice

class Notification(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    devices = models.ManyToManyField(FCMDevice)
