from dataclasses import dataclass
import datetime
from datetime import time
from random import randrange
import csv
import os
import flask
import requests
from flask import jsonify
from flask import request as flask_request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@dataclass
class event:
    day: str = ""
    day_nb: int = 0
    begins: time = time(0, 0)
    duration: int = 0


modules = {}

week_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]


def create_modules_events():
    global week_days
    events = []
    number_of_events = randrange(1, 4)
    first_day = randrange(0, 4)
    for i in range(number_of_events):
        first_day = (randrange(1, 3) + first_day) % 5
        begins = randrange(0, 7) + 8
        duration = randrange(1, 4)
        new_event = event(week_days[first_day],
                          first_day, time(begins, 0), duration)
        events.append(new_event)
    return (events)


@app.route('/', methods=['GET'])
def getByName():
    global modules
    query = flask_request.args.get('modules', None)
    print(query)
    if query is None:
        return jsonify(modules)
    else:
        modules_list = query.split(',')
        ret = {}
        for i in modules_list:
            if i in modules:
                ret[i] = modules[i]
            else:
                ret[i] = "Not Found"
        return jsonify(ret)


def create_modules():
    global modules
    modules = {}
    with open(os.path.dirname(os.path.realpath(__file__)) + '/data') as fd:
        reader = csv.reader(fd)
        for row in reader:
            modules[row[0]] = {}
            modules[row[0]]['name'] = row[1]
            events = create_modules_events()
            modules[row[0]]['events'] = {}
            z = 0
            for i in events:
                modules[row[0]]['events'][i.day] = {}
                modules[row[0]]['events'][i.day]['begins'] = i.begins.strftime(
                    "%H:%M")
                modules[row[0]]['events'][i.day]['duration'] = i.duration
                z += 1


create_modules()
app.run()
