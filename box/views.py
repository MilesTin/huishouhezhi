#_*_  coding:utf-8 _*_
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse
from .models import heZhi
from django.forms.models import model_to_dict
import json
import datetime
# Create your views here.


def getall(request):
    boxes = heZhi.objects.all().values()
    data = list(boxes)
    return JsonResponse(data,safe=False)


def getbox(request, boxId):
    obj = get_object_or_404(heZhi,pk=boxId)
    data = model_to_dict(obj)
    return JsonResponse(data, safe=False)

def getBoxCount(date:datetime.date):
    sum = 0

    boxes = heZhi.objects.filter(date=date).values()
    for box in boxes:
        sum += box['lunchBoxCount']
    return sum

def getLunchBoxCount(request):
    try:
        year = int(request.GET.get("year", 0))
        month = int(request.GET.get("month", 0))
        day = int(request.GET.get("day", 0))
    except ValueError:
        return JsonResponse({"errmsg": "未知错误"}, status=404)
    #返回当天所有餐盒收集箱使用的餐盒数
    if not year or not month or not day:
        return JsonResponse({'errmsg':'year month or day字段缺失'},status=404)
    try:
        date = datetime.date(year,month,day)
    except ValueError:
        return JsonResponse({'errmsg':"invalid date {}/{}/{}".format(year,month,day)},status=404)
    sum = 0

    boxes = heZhi.objects.filter(date=date).values()
    for box in boxes:
        sum += box['lunchBoxCount']

    return JsonResponse({'count':sum})

def getSevenDayAvg(request):
    try:
        year = int(request.GET.get("year",0))
        month = int(request.GET.get("month",0))
        day = int(request.GET.get("day",0))
    except ValueError:
        return JsonResponse({"errmsg":"未知错误"},status=404)
    if not year or not month or not day:
        return JsonResponse({'errmsg':'year month or day字段缺失'},status=404)
    try:
        date = datetime.date(year,month,day)
    except ValueError:
        return JsonResponse({'errmsg':"invalid date {}/{}/{}".format(year,month,day)},status=404)

    sum = 0
    delta1Day = datetime.timedelta(-1)
    boxes = []
    for i in range(7):
        count = getBoxCount(date)
        sum += count
        boxes.append(count)
        date += delta1Day
    boxes.reverse()
    avg = sum/7
    return JsonResponse({'boxAvg':avg,'boxSum':sum,'boxes':boxes})

#GET传入boxid
def box_clean(request):
    boxid = request.GET.get("boxid","")
    cur_box = get_object_or_404(heZhi,id=boxid)
    cur_box.space = None
    cur_box.save()
    return JsonResponse({"msg":"successful clean box"})

def space(request):
    """
    :param request
    GET 方法传入
    boxid
    :return:
    """
    boxid = request.GET.get("boxid","")
    cur_box = get_object_or_404(heZhi,id=boxid)
    return JsonResponse({"count":cur_box.space})
