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

    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
	}

    modulesPerDay = { 0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[] }

    if "modules" in context:
        webservice_url += "?modules=" + context['modules']
    modulesInfos = requests.get(webservice_url).json()

    for module in modulesInfos:
        moduleName = module  + " - " + modulesInfos[module]['name']
        for i in modulesInfos[module]['events']:
            modulesPerDay[int(i)].append({
                "begins": modulesInfos[module]['events'][i]['begins'],
                "duration": modulesInfos[module]['events'][i]['duration'],
                "module": moduleName
            })
            # print(modulesInfos[module]['events'][i]['begins'], "for", modulesInfos[module]['events'][i]['duration'])
        # print(moduleName)

    return render(request, 'dashboard/index.html', context)