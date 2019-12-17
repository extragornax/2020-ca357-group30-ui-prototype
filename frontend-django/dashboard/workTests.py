import requests

webservice_url = 'http://vps.cheap.appboxes.co:10126/'
webservice_url = 'http://vps.cheap.appboxes.co:10126/?modules=CA146,CA377'
modulesInfos = requests.get(webservice_url).json()
# print(modulesInfos)

context = {}

modulesPerDay = [{"day": "Monday", "data": []}, {"day": "Tuesday", "data": []}, {"day": "Wednesday", "data": []},
                 {"day": "Thursday", "data": []}, {"day": "Friday", "data": []}, {"day": "Saturday", "data": []}, {"day": "Sunday", "data": []}]

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
        print("Pop", counter, i['day'])
        toPop.append(counter)
    counter += 1
while len(toPop) > 0:
    index = toPop.pop()
    print("pop ", index, modulesPerDay[index]['day'])
    modulesPerDay.pop(index)

print(modulesPerDay)

context['modulesPerDay'] = modulesPerDay
