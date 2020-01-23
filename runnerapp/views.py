from django.shortcuts import render
from django.utils import timezone
import pytz
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Count
from django.db.models import Max
from django.db.models import Sum
from dss.Serializer import serializer
import requests
import json
import random
import datetime
import xmltodict
import uuid
import  time
import base64
from Crypto.Cipher import AES
import requests
import json

# Participate
from .models import User,Plan,JoinPlan,Table_1,Table_2,Table_3,Table_4

# 1440751417.283 --> '2015-08-28 16:43:37.283'
def timestamp2string(timeStamp):
    try:
        d = datetime.datetime.fromtimestamp(timeStamp)
        str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
        # 2015-08-28 16:43:37.283000'
        return str1
    except Exception as e:
        print(e)
        return ''

class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        print(1)
        print(self.sessionKey)
        sessionKey = base64.b64decode(self.sessionKey)
        print(2)
        print(sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        print(3)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)

        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))

        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

#文件下载
def handle_upload_file(file,filename,path):
    allpath = 'uploads/'+path
    #上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(allpath):
        os.makedirs(allpath)
    with open(allpath+filename,'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return path+filename

def getwxinfor(code):
    appid = 'wx5b35e1d11ff77a12'
    appSecret = '11b0f90ce0e6d4646ca18af0257e7ef6'
    url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code" % (
        appid, appSecret, code)
    req = requests.get(url)
    rep = req.json()
    print(rep)
    return rep

def getwxphone(code,iv,encryptedData):
    appid = 'wx5b35e1d11ff77a12'
    rep=getwxinfor(code)
    sessionKey=rep.get("session_key")
    pc = WXBizDataCrypt(appid, sessionKey)
    infor = pc.decrypt(encryptedData, iv)
    phone=infor.get("purePhoneNumber")
    return phone

@csrf_exempt
def login(request):
    if request.method == "GET":
        picture=request.GET.get('picture')
        code = request.GET.get('code')
        nickname = request.GET.get('nickname')
        gender=request.GET.get('gender')
        appid = 'wx5b35e1d11ff77a12'
        appSecret = '11b0f90ce0e6d4646ca18af0257e7ef6'
        data = {
            'appid': appid,
            'secret': appSecret,
            'js_code': code,
            'grant_type': 'authorization_code',
        }
        url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code" % (
            appid, appSecret, code)
        r = requests.get(url=url)
        response = r.json()
        openid = response['openid']
        account = User.objects.filter(openid=openid).exists()
        if account:
            newaccount = User.objects.get(openid=openid)
            if newaccount.status == 0:
                return JsonResponse({"userid": newaccount.userid,"status":0})
            else:
                return JsonResponse({"userid": newaccount.userid, "status": 1})
        else:
            newaccount=User.objects.create(openid=openid, nickname=nickname, picture=picture, gender=gender, status=0)
            return JsonResponse({"userid":newaccount.userid,"status":0})

def getphone(request):
    if request.method=='GET':
        userid=request.GET.get('userid','')
        code=request.GET.get('code','')
        iv = request.GET.get('iv', '')
        encryptedData = request.GET.get('encryptedData', '')
        phone=getwxphone(code,iv,encryptedData)
        print(phone)
        try:
            user=User.objects.get(userid=userid)
            user.telephone=phone
            user.status=1
            user.save()
            return JsonResponse({"success": True})
        except:
            return JsonResponse({"success":False})


def del_repeat(list,key):
    newList=[]
    newList.append(list[0])
    for dict in list:
        k=0
        for item in newList:
            if dict[key] != item[key]:
                k=k+1
            else:
                break
            if k == len(newList):
                newList.append(dict)
    return newList


######################################################################################

def uploadPlan(request):
    if request.method=='GET':
        user_id=request.GET.get('user_id','')
        plan_content=request.GET.get('plan_content','')
        plan_type = request.GET.get('plan_type', '')
        plan_speed = request.GET.get('plan_speed', '')
        plan_place = request.GET.get('plan_place', '')
        plan_mileage = request.GET.get('plan_mileage', '')

        user = User.objects.get(user_id=user_id)
        now = datetime.datetime.now()
        new_data = Plan.objects.create(plan_content=plan_content, plan_type=plan_type, plan_speed=plan_speed, plan_place=plan_place,
                                       plan_mileage=plan_mileage,plan_manager=user,time=now)

        new_id = new_data.plan_id
        Plan_data = Plan.objects.filter(plan_id=new_id).values('plan_id')
        Plan_data = serializer(Plan_data)
        return JsonResponse({'data': Plan_data, 'state': 'success'})


def getPlan(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id','')
        user = User.objects.get(user_id=user_id)

        #此处的数据有冗余，花了2h未找到合适解决方法--distinct
        Plan_data=Plan.objects.filter(plan_manager=user).values('plan_manager', 'joinplan__user', 'joinplan__time', 'plan_place', 'plan_id', 'plan_place',
               'plan_content', 'plan_mileage', 'plan_speed','plan_type')
        Plan_data=serializer(Plan_data)

        # print('old:',Plan_data)
        # 找了一个函数解决了，不知道为什么出现此问题
        Plan_data=del_repeat(Plan_data,'plan_id')
        # print('new:', Plan_data)

        Join_data=JoinPlan.objects.filter(user=user).values('user__nickname','user__picture','user_id')
        Join_data = serializer(Join_data)

        return JsonResponse({'plan': Plan_data,'Join_data':Join_data})


def joinPlan(request):
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        plan_id =request.GET.get("plan_id")
        detail =request.GET.get("detail")


        user = User.objects.get(user_id=user_id)
        plan = Plan.objects.get(plan_id=plan_id)

        now = datetime.datetime.now()



        newJoin = JoinPlan.objects.create(plan=plan,detail=detail,user=user,time=now)
        newJoin = serializer(newJoin)

        return JsonResponse({'data': newJoin,"state": 'success' })


def getJoinUsers(request):
    if request.method == "GET":
        plan_id =request.GET.get("plan_id")
        # user_id =request.GET.get("user_id")
        plan = Plan.objects.get(plan_id=plan_id)

        newJoin = JoinPlan.objects.filter(plan=plan)
        newJoin = serializer(newJoin)
        #
        # manager= Plan.objects.filter(plan_manager_id=user_id)
        # manager = serializer(manager)
        return JsonResponse({'join': newJoin,"state": 'success' })


def getTable(request):
    if request.method == "GET":

        t1 = Table_1.objects.all()
        t2 = Table_2.objects.all()
        t3 = Table_3.objects.all()
        t4 = Table_4.objects.all()

        t1 = serializer(t1)
        t2 = serializer(t2)
        t3 = serializer(t3)
        t4 = serializer(t4)
        #
        # manager= Plan.objects.filter(plan_manager_id=user_id)
        # manager = serializer(manager)
        return JsonResponse({'data': [t1,t2,t3,t4], "state": 'success'})