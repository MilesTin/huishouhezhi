from django.db import models

# Create your models here.

class heZhi(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    iconPath = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
