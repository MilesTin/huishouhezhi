from django.db import models
from login.models import user
from box.models import heZhi
# Create your models here.
class order(models.Model):
    inCompleted = 0
    completed = 1
    needAdmin = 2#超时未完成
    STATUS_CHOICES = (
        (inCompleted,"inCompleted"),
        (completed,"completed"),
        (needAdmin,"needAdmin")
    )

    timedel= models.IntegerField(default=5)
    id = models.CharField(max_length=30,unique=True,primary_key=True)#餐盘id就行
    created_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    user = models.ForeignKey(user,on_delete=models.CASCADE,related_name="user_order")
    box = models.ForeignKey(heZhi,default=None,null=True,related_name="box_order",on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    endedTime = models.DateField(null=True,blank=True)
