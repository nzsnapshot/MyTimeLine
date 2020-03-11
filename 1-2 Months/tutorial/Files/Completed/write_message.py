# filename = 'programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming\n")
#     file_object.write("I love creating new games\n")

filename = 'programming.txt'
with open(filename, 'a') as f:
    f.write("I also love finding meaning in new datasets\n")
    f.write("I love creating pornhub apps\n")