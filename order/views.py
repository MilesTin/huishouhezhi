from django.shortcuts import render
from django.http import  JsonResponse
from django.shortcuts import get_object_or_404,redirect
from login.models import *
from .models import *
import datetime
from datetime import timedelta
# Create your views here.


def new_order(request):#必须先登录
    update_db()
    openid = request.session.get("openid")
    orderid = request.GET.get("id")
    if not openid:
        redirect("/account/login")

    if not orderid:
        return JsonResponse({"msg":"餐盒id字段为空"},status=404)

    cur_user = get_object_or_404(user,openid=openid)

    if order.objects.filter(id=orderid,status=order.inCompleted) or order.objects.filter(id=orderid,status=order.needAdmin):
        return JsonResponse({'msg':'餐盒已有人使用'},status=404)

    new_order = order.objects.create(user=cur_user,id=orderid,status=order.inCompleted)
    new_order.save()

    return JsonResponse({'msg':'order is successful'})

def verif_order(request):
    #
    update_db()
    openid = request.GET.get("openid")
    orderid = request.GET.get('id')

    if not openid:
        redirect("/account/login")

    if not orderid:
        return JsonResponse({"msg": "餐盒id字段为空"}, status=404)


    cur_user = get_object_or_404(user, openid=openid)

    finded_order = get_object_or_404(order,user=cur_user,id=orderid,status=order.inCompleted)

    return JsonResponse({'exist':True})

def order_complete(request):
    openid = request.GET.get("openid")
    orderid = request.GET.get('id')

    if not openid:
        redirect("/account/login")

    if not orderid:
        return JsonResponse({"msg": "餐盒id字段为空"}, status=404)

    cur_user = get_object_or_404(user, openid=openid)

    finded_order = get_object_or_404(order, user=cur_user, id=orderid, status=order.inCompleted)
    finded_order.status = order.completed
    finded_order.save()
    return JsonResponse({"msg":"complete order successful"})

def update_db():
    for cur_order in order.objects.all():
        timedel =timedelta(cur_order.timedel)
        today = datetime.date.today()
        if (today-cur_order.created_date) > timedel:
            if cur_order.status==order.inCompleted:
                cur_order.status = order.needAdmin
                cur_order.save()




