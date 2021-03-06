from django.shortcuts import render
import requests
from dashboard.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import date
# Index route


def cleanModulesSearch(s):
    s = s.replace(" ", "")
    s = s.upper()
    return s


def login(request):
    return render(request, 'dashboard/login.html')


@csrf_exempt
def register(request):
    context = {}
    if request.method == 'POST':
        User.objects.filter(modules=request.POST['modules']).delete()
        user = User(first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    dcu_id=request.POST['dcu_id'],
                    modules=request.POST['modules'])
        user.save()
        context['msg'] = "Register Successfull"
        return render(request, 'dashboard/login.html', context=context)
    return render(request, 'dashboard/register.html')


def index(request):
    context = {}
    webservice_url = 'http://vps.cheap.appboxes.co:10126/'
    announcements = []
    modules_error = ""
    if "dcu_id" in request.GET:
        context['dcu_id'] = request.GET['dcu_id']
        context['modules'] = User.objects.filter(
            dcu_id=request.GET['dcu_id'])
        if not context['modules']:
            context['modules'] = ""
        else:
            context['modules'] = User.objects.filter(
                dcu_id=request.GET['dcu_id'])[0].modules
    elif "modules" in request.GET:
        context['modules'] = cleanModulesSearch(request.GET['modules'])
    if "announcements" in request.GET:
        context['announcements'] = request.GET['announcements']

    modulesPerDay = [{"day": "Monday", "data": []}, {"day": "Tuesday", "data": []}, {"day": "Wednesday", "data": []},
                     {"day": "Thursday", "data": []}, {"day": "Friday", "data": []}, {"day": "Saturday", "data": []}, {"day": "Sunday", "data": []}]

    if "modules" in context and len(context['modules']) > 0:
        webservice_url += "?modules=" + cleanModulesSearch(context['modules'])
    else:
        webservice_url += "?modules=CA377%2CCA268%2CCA357%2CCA358%2CCA349%2CCA392"

    modulesInfos = requests.get(webservice_url).json()
    for module in modulesInfos:
        if modulesInfos[module] != "Not Found":
            moduleName = module + " - " + modulesInfos[module]['name']
            if modulesInfos[module]['announcement'] != "None":
                announcements.append(
                    {'module': moduleName, "info": modulesInfos[module]['announcement']})
            for i in modulesInfos[module]['events']:
                timeSplitStart = modulesInfos[module]['events'][i]['begins'].split(
                    ':')
                timeSplitEnd = modulesInfos[module]['events'][i]['ends'].split(
                    ':')
                classData = {
                    "start_hour": timeSplitStart[0],
                    "start_min": timeSplitStart[1],
                    "end_hour": timeSplitEnd[0],
                    "end_min": timeSplitEnd[1],
                    "duration": modulesInfos[module]['events'][i]['duration'],
                    "module": moduleName
                }
                modulesPerDay[int(i)]['data'].append(classData)
        else:
            if len(modules_error) == 0:
                modules_error += "Some modules were not found, please note only CA modules are available please recheck : "
            modules_error += module + " "
    counter = 0
    toPop = []
    lectCounter = 0
    today = date.today().weekday()
    for i in modulesPerDay:
        if len(i['data']) == 0:
            toPop.append(counter)
        if counter == today:
            lectCounter = len(i['data'])
        counter += 1
    earliestTime = {"hour": None, "min": None}
    for i in modulesPerDay[today]['data']:
        if earliestTime['hour'] == None:
            earliestTime['hour'] = i['start_hour']
            earliestTime['min'] = i['start_min']
        elif earliestTime['hour'] == i['start_hour']:
            if earliestTime['min'] > i['start_min']:
                earliestTime['min'] = i['start_min']
        elif earliestTime['hour'] == i['start_hour']:
            earliestTime['hour'] = i['start_hour']
            earliestTime['min'] = i['start_min']

    while len(toPop) > 0:
        modulesPerDay.pop(toPop.pop())

    context['modulesPerDay'] = modulesPerDay
    context['lectureCount'] = {"count": lectCounter, "first": earliestTime}
    context['announcements'] = announcements

    context['modules_error'] = modules_error
    return render(request, 'dashboard/index.html', context)
