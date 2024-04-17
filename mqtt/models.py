from django.db import models

# Create your models here.


class Message(models.Model):
    user_id = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    volume = models.FloatField()
    iswearing = models.BooleanField()
    isfall = models.BooleanField()
    onfire = models.BooleanField()
    workStatus = models.IntegerField()
    location = models.IntegerField()
    timestamp = models.DateTimeField()
    iscall = models.BooleanField()
    voiceCommand = models.CharField(max_length=100)
    gesture = models.IntegerField()

    def __str__(self):
        return self.id
