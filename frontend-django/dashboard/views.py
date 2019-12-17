from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
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
    for i in modulesPerDay:
        if len(i['data']) == 0:
            toPop.append(counter)
        counter += 1
    while len(toPop) > 0:
        modulesPerDay.pop(toPop.pop())

    context['modulesPerDay'] = modulesPerDay

    return render(request, 'dashboard/index.html', context)