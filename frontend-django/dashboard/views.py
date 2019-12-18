from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from datetime import date
# Index route


def index(request):
    context = {}
    if "modules" in request.GET:
        context['modules'] = request.GET['modules']
    if "announcements" in request.GET:
        context['announcements'] = request.GET['announcements']
    webservice_url = 'http://vps.cheap.appboxes.co:10126/'

    modulesPerDay = [{"day": "Monday", "data": []}, {"day": "Tuesday", "data": []}, {"day": "Wednesday", "data": []},
                     {"day": "Thursday", "data": []}, {"day": "Friday", "data": []}, {"day": "Saturday", "data": []}, {"day": "Sunday", "data": []}]

    if "modules" in context and len(context['modules']) > 0:
        webservice_url += "?modules=" + context['modules']
    else:
        webservice_url += "?modules=CA377%2CCA268%2CCA357%2CCA358%2CCA349%2CCA392"
    modulesInfos = requests.get(webservice_url).json()

    for module in modulesInfos:
        moduleName = module + " - " + modulesInfos[module]['name']
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
    return render(request, 'dashboard/index.html', context)
