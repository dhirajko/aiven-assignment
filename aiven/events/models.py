from django.db import models
from django.utils import timezone


class Event(models.Model):
    event_id:models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=20)
    event_location = models.CharField(max_length=20)
    date = models.DateTimeField(blank=False, default=timezone.now())
    phone = models.IntegerField()


    def __str__(self):
        return self.event_name + " at " +self.event_location