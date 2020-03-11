import tkinter as tk
import time
import json
import datetime

with open('/Users/Snapshot/Downloads/AutoTimer-master/backup/activities.json') as f:
    data = json.load(f)
# print(data)
all_dict = data["activities"]


def checkappend(appendto: list, fromdict: dict, key: str,):
    if key in fromdict:
        appendto.append( fromdict[key] )

windows = []
time = []
secs = []
mins = []
hours = []

for i in all_dict:
    checkappend(windows, i, 'name')
# print(all_dict[0])
def auto_tracker(pos_in_json):
    list_var = all_dict[pos_in_json]["name"]
    print(list_var)
    for k in all_dict[pos_in_json]['time_entries']:
        save = k
        # TODO: Its here somewhere that its fucked
        for sec in str(save['seconds']):
            secs.append(int(sec))
        for min in str(save['minutes']):
            mins.append(int(min))
        for hour in str(save['hours']):
            hours.append(int(hour))
        ##############################
    seconds = secs
    # minutes = sum(mins)
    # hour = sum(hours)
    print(seconds)
    # a = seconds
    # min = minutes * 60
    # hr = hour * 60
    # m = hr * 60
    # total_seconds = seconds + min + m
    # print(minutes)
    # print(f"Total seconds: {total_seconds}")
    # b = str(datetime.timedelta(seconds=total_seconds))
    # b = seconds % 3600 // 60
    # c = seconds % 3600 % 60
    # d = "{} hours {} mins {} seconds".format(a, b, c)
    # return b

list_var = all_dict[0]["name"]

wind = len(windows)
num = 0


# Below chnage the 8 to any number
print(auto_tracker(5))
print(auto_tracker(1))


# for x in range(1, wind):
#     print(auto_tracker())












#     checkappend(time, i, 'time_entries')
    # for x in time:
    #     save = x
    # print(save)
    # for y in save:
    #     if 'seconds' in y[0]:

    #         seconds = checkappend(secs, y, 'seconds')
        # minutes = checkappend(mins, y, 'minutes')
        # hour = checkappend(hours, y, 'hours')
        # if 'seconds' in x:
        #     checkappend(secs, x, int)
        # if 'minutes' in x:
        #     checkappend(mins, x, int)


# print(secs)
# print(mins)
# print(hours)

''' somewhat works'''
# print(secs)
# print(secs)
# num = 0
# print(windows[0])
# l = len(time[num])
# l -= 1 
# print(time[0][l]['seconds'])
###########################


# time_ent = []
# for i in all_dict:
#     try:
#         name = i["name"]
#         time = i["time_entries"]
#     except KeyError:
#         pass
#     else:
#         windows.append(name)
#         time_ent.append(time)



# new_dict = time_ent
# secs = []
# num = 0
# for k in new_dict:
#     try:
#         seconds = k
#     except KeyError:
#         pass
#     else:
#         secs.append(seconds)

# for x in secs:
#     print(x[0])








# print(secs)
# print(windows)


# for k, v in data.items():
# actvities = []
#     actvities.append(v)

# print(actvities[0][0])
# windows = []
# num = 0
# name_windows = data["activities"][0]["name"]
# # for x in data["activities"][num]["name"]:
# for v in data["activities"][num]:
#     print(name_windows)
#     windows.append(name_windows)
#     num += 1
#     print(windows)
#     name_windows = data["activities"][num]["name"]
#     num +=1 
#     windows.append(name_windows)
# print(windows)
# print(data["activities"][1]["time_entries"][0]["seconds"])



# secs = []
# for x in time_ent:
#     try:
#         seconds = x[0]

#     except KeyError:
#         pass
#     else:
#         secs.append(seconds)