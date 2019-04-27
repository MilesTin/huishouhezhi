from django.db import models



class user(models.Model):
    openid = models.CharField(max_length=30,unique=True,primary_key=True)
    updated = models.DateTimeField(auto_now=True)
