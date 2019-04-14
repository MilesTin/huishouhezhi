from django.db import models

# Create your models here.

class account(models.Model):

    openid = models.CharField(max_length=30)
    unionid = models.CharField(max_length=30)

    def __str__(self):
        return "openid:"+self.openid

