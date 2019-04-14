from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import urllib.request
import json





def login(request):
    appid = request.GET.get("appid","")
    secret = request.GET.get("secret","")
    code = request.GET.get("code","")
    errmsg = ""
    if not appid:
        errmsg+= "appid不能为空"
    elif not secret:
        errmsg+="秘钥secret不能为空"
    elif not code:
        errmsg+="登录code为空"

    if  errmsg:
        return JsonResponse({"errmsg":errmsg},status=404)

    #发送请求获得openid session_key unionid errcode errmsg

    tencent_url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(appid,secret,code)


    headers = {'content-type':'application/json'}

    R = urllib.request.Request(url=tencent_url,headers=headers)

    response = urllib.request.urlopen(R).read()

    response_json = json.loads(response)
    openid=response_json.get("openid")
    session_key = response_json.get("session_key")
    unionid = response_json.get("unionid")
    errmsg = response_json.get("errmsg","")
    errcode = response_json.get("errcode")

    if errcode==0:
        request.session['openid'] = openid
        request.session['unionid'] = unionid
        request.session.set_expiry(100000000)
        return JsonResponse({"msg":"You are logged"})
    else:#errcode由微信api决定(auth code2session), https://developers.weixin.qq.com/miniprogram/dev/api-backend/auth.code2Session.html
        return JsonResponse({"errmsg": errmsg,"errcode":errcode}, status=404)

def logout(request):
    if request.session.exists('openid'):
        del request.session['openid']
    if request.session.exists('unionid'):
        del request.session['unionid']
    return JsonResponse({"msg":"You are logged out"})
