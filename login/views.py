from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import urllib.request
import json
import datetime
from django.conf import settings
from .models import *
from order.models import *

def login(request):
    appid = settings.APPID
    secret = settings.SECRET
    code = request.GET.get("code","")
    errmsg = ""
    if not code:
        errmsg += "code不存在"

    if errmsg:
        return JsonResponse({"errmsg":errmsg},status=404)

    #发送请求获得openid session_key unionid errcode errmsg

    tencent_url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(appid,secret,code)


    headers = {'content-type':'application/json'}

    R = urllib.request.Request(url=tencent_url,headers=headers)#接口成功只返回openid session_key

    response = urllib.request.urlopen(R).read()

    response_json = json.loads(response)
    openid=response_json.get("openid")
    session_key = response_json.get("session_key")
    unionid = response_json.get("unionid")
    errmsg = response_json.get("errmsg","")
    errcode = response_json.get("errcode")

    if not errcode:
        request.session['openid'] = openid
        if not user.objects.filter(openid=openid):#用户没有注册（登录过）
            obj = user()
            obj.openid = openid
            obj.save()
        request.session['session_key'] = session_key
        request.session.set_expiry(100000000)
        return JsonResponse({"msg":"You are logged in"})
    else:#errcode由微信api决定(auth code2session), https://developers.weixin.qq.com/miniprogram/dev/api-backend/auth.code2Session.html
        return JsonResponse({"errmsg": errmsg,"errcode":errcode}, status=404)


def logout(request):
    if request.session.exists('openid'):
        del request.session['openid']
    if request.session.exists('session_key'):
        del request.session['session_key']
    return JsonResponse({"msg":"You are logged out"})

#需要登录
def order_count(request):
    openid = request.session.get("openid","")

    cur_user = get_object_or_404(user,openid=openid)
    #返回用户所有的订单数 包括3个状态
    counts = len(cur_user.user_order.all())
    return JsonResponse({"count":counts})

def days_sum(request):
    openid = request.session.get("openid","")
    cur_user = get_object_or_404(user, openid=openid)
    sum = 0
    for orderObj in order.objects.filter(user=cur_user):
        endTime = orderObj.endedTime
        createdTime = orderObj.created_date
        if not endTime:
            sum += (datetime.datetime.today().date() - createdTime).days
        else:
            sum += (endTime - createdTime).days

    return JsonResponse({'count': sum})

def enery_sum(request):
    openid = request.session.get("openid", "")
    cur_user = get_object_or_404(user, openid=openid)
    return JsonResponse({"energy_saved":cur_user.energy_saved})

def enery_unsaved(request):
    openid = request.session.get("openid", "")
    cur_user = get_object_or_404(user, openid=openid)
    return JsonResponse({"energy_saved": cur_user.energy_saved})

#回收能量池中能量到energy_saved
def save_energy(request):
    openid = request.session.get("openid", "")
    cur_user = get_object_or_404(user, openid=openid)
    if cur_user.energy_unsaved<=0:
        return JsonResponse({"msg":"没有能量值剩下了"},status=404)
    cur_user.energy_saved += cur_user.energy_unsaved
    cur_user.energy_unsaved = 0
    return JsonResponse({'msg':"saved successful"})