import tkinter as tk
import time
import json
import datetime

with open('/Users/Snapshot/Downloads/AutoTimer-master/backup/activities.json') as f:
    data = json.load(f)
    activities_dict = data["activities"]

seconds = []

for i in range(len(activities_dict)):
    for time_units in activities_dict[i]['time_entries']:
        print(activities_dict[1]['name'])
        print(f"Date: {time_units['start_time'][:time_units['start_time'].index(' ')]}")
        print(f"Seconds: {time_units['seconds']}")
        print(f"Minutes: {time_units['minutes']}")
        print(f"Hours: {time_units['hours']}\n")



