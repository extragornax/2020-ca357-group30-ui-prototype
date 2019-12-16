import requests

webservice_url = 'http://vps.cheap.appboxes.co:10126/'
webservice_url = 'http://vps.cheap.appboxes.co:10126/?modules=CA146,CA377'
modulesInfos = requests.get(webservice_url).json()
# print(modulesInfos)
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
for i in modulesPerDay:
	print(days[i], end=" ")
	if len(modulesPerDay[i]) == 0:
		print("None")
	else:
		print(modulesPerDay[i])
