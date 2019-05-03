from django.db import models
import datetime
from order.models import *
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

    lunchBoxCount = models.IntegerField(default=0)
    date = models.DateField("日期",auto_now_add=True)
    space = models.IntegerField(default=50)
    def __str__(self):
        return self.name

