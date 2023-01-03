from django.shortcuts import render, HttpResponse
from app01 import models

import json
import time
import datetime
import pytz as pytz


# Create your views here.


def index(request):
    return HttpResponse("hello, my friend\n")


def index_1(request):
    return render(request, "1.html")


def index_2(request):
    name = 'yk'
    name1 = ['12', '34', '56', '78']
    return render(request, "tpl.html", {'n1': name, 'n2': name1})


def count(request):
    cnt = models.a.objects.filter(id=1)
    if request.method == "POST":
        cnt.update(cnt=cnt.first().cnt+1)
    # if request.method == "GET":
    return render(request, "cnt.html", {"cntdata": cnt.first()})
    # models.a.objects.create(cnt=1)


def add_(request):
    return HttpResponse("hello, my friend\n")


def set_aircon(request):
    airset = models.air_set.objects
    airset.update(if_on=1)
    if request.method == "POST":
        print(request.POST)
        airset.update(temp=request.POST["wendu"])
        airset.update(mode=request.POST["moshi"])
        airset.update(speed=request.POST["fengsu"])
    return render(request, "set_air.html", {"set": airset.first(), "cishu": range(4), "wendu": range(23, 27)})


# def set_day1(request):
#     if request.method == "POST":
#         print(request.POST)

#     return render(request, "adsfg.html")


def zlh(request):
    airset = models.air_set.objects
    if_onn = airset.first().if_on
    airset.update(if_on=0)
    jso = {"if_change": if_onn, "set": {
        "windSpeed": airset.first().speed, "needTemperature": airset.first().temp, "Mode": airset.first().mode, "personalMode": airset.first().pref, "on_off": airset.first().on_off}, }
    return HttpResponse(json.dumps(jso))


def create(request):
    shuju = models.week_time
    a = ["一", "二", "三", "四", "五", "六", "七"]
    for i in a:
        for j in range(1, 49, 1):
            shuju.objects.create(times_start=j, week_num="周".join(
                i), if_on=0, times_start_show=f"{str(int((j-1)/2))}:{str((j+1)%2*30)}")


def sleep(request):
    modemap = {0: 'auto', 1: 'dry', 2: 'cold', 3: 'wind', 4: 'hot'}
    week_time = models.week_time
    a = ["一", "二", "三", "四", "五", "六", "七"]
    if request.method == "POST":
        #     print(request.POST)
        #     for p in range(1, 49, 1):
        #         week_time.objects.filter(times_start=p).update(if_on=0)
        # for i in request.POST.keys:
        # for j in a:
        # if i == j:
        for i in a:
            if request.POST.getlist(i) != []:
                week_time.objects.filter(week_num=i).update(if_on=0)
            for p in request.POST.getlist(i):
                # if p != []:
                #     week_time.objects.filter(
                #         week_num=i).update(if_on=0)
                week_time.objects.filter(
                    week_num=i, times_start=int(p)).update(if_on=1)

    airset = models.air_set.objects
    # airset.update(if_on=1)
    if request.method == "POST":
        print(request.POST)
        if request.POST.getlist("wendu") != []:
            airset.update(if_on=1)
            airset.update(temp=request.POST.getlist("wendu")[0])
            airset.update(mode=request.POST.getlist("moshi")[0])
            airset.update(speed=request.POST.getlist("fengsu")[0])
            airset.update(pref=request.POST.getlist("pianhao")[0])
            airset.update(on_off=request.POST.getlist("123")[0])

    data_list_1 = week_time.objects.filter(week_num="一").all()
    data_list_2 = week_time.objects.filter(week_num="二").all()
    data_list_3 = week_time.objects.filter(week_num="三").all()
    data_list_4 = week_time.objects.filter(week_num="四").all()
    data_list_5 = week_time.objects.filter(week_num="五").all()
    data_list_6 = week_time.objects.filter(week_num="六").all()
    data_list_7 = week_time.objects.filter(week_num="七").all()
    # return render(request, "index2.html", {"Mon_hourtime": data_list_1, "Tues_hourtime": data_list_2, "Wen_hourtime": data_list_3, "Thur_hourtime": data_list_4, "Fri_hourtime": data_list_5, "Sat_hourtime": data_list_6, "Sun_hourtime": data_list_7, "cishu": range(4), "set": airset.first(), "wendu": range(23, 27)})
    return render(request, "butify.html", {"Mon_hourtime": data_list_1, "Tues_hourtime": data_list_2, "Wen_hourtime": data_list_3, "Thur_hourtime": data_list_4, "Fri_hourtime": data_list_5, "Sat_hourtime": data_list_6, "Sun_hourtime": data_list_7, "cishu": range(4), "set": airset.first(), "wendu": range(20, 27), "modemap": modemap, })


def zlh2(request):
    weeks = ["一", "二", "三", "四", "五", "六", "七"]
    tz = pytz.timezone('Asia/Shanghai')
    t = datetime.datetime.fromtimestamp(int(time.time()), tz)
    hourr = t.hour
    minn = t.min
    week_time = models.week_time.objects.filter(
        week_num=weeks[t.weekday()], times_start=1+int(t.strftime('%H'))*2+int(int(t.strftime('%M'))/30)).all().first()
    # local_time = time.localtime(time.time())
    return HttpResponse(week_time.if_on)
