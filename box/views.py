#_*_  coding:utf-8 _*_
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse
from .models import heZhi
from django.forms.models import model_to_dict
import json
# Create your views here.


def getall(request):
    boxes = heZhi.objects.all().values()
    data = list(boxes)
    return JsonResponse(data,safe=False)


def getbox(request, boxId):
    obj = get_object_or_404(heZhi,pk=boxId)
    data = model_to_dict(obj)
    return JsonResponse(data, safe=False)

