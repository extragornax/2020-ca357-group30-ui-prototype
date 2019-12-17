from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
# Index route


def cleanModulesSearch(s):
    s = s.replace(" ", "")
    s = s.upper()

    return s


def index(request):
    context = {}
    if "modules" in request.GET:
        context['modules'] = cleanModulesSearch(request.GET['modules'])
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

    modulesPerDay = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

    modules_error = ""
    if "modules" in context:
        print(str(context['modules']))
        webservice_url += "?modules=" + cleanModulesSearch(context['modules'])
    modulesInfos = requests.get(webservice_url).json()
    for module in modulesInfos:
        if modulesInfos[module] != "Not Found":
            moduleName = module + " - " + modulesInfos[module]['name']
            for i in modulesInfos[module]['events']:
                modulesPerDay[int(i)].append({
                    "begins": modulesInfos[module]['events'][i]['begins'],
                    "duration": modulesInfos[module]['events'][i]['duration'],
                    "module": moduleName
                })
        else:
            if len(modules_error) == 0:
                modules_error += "Some modules were not found, please note only CA modules are available please recheck : "
            modules_error += module + " "

    context['modules_error'] = modules_error
    return render(request, 'dashboard/index.html', context)
