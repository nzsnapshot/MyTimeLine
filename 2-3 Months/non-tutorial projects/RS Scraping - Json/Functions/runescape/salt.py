import json

with open('readable_eq_data.json') as f:
    summary = json.load(f)

my_dict = summary

my_list = []
for attribute in summary:
    item = my_dict.get(attribute)
    if item:
        my_list.append(item)

print(my_list)


# my_dict = {"name":"Bob", "age":25, "sex":"M","location":"somewhere"}
#
# my_list = []
# for attribute in ["name", "age", "race", "income"]:
#     item = my_dict.get(attribute)
#     if item:
#         my_list.append(item)
#
#
#
#
# my_dict = {"name": "Bob", "age": 25, "sex": "M", "location": "somewhere"}
# what_i_want = ["name", "age", "race", "income"]
# what_i_get = [v for k, v in my_dict.items() if k in set(what_i_want)]
# print(what_i_get)