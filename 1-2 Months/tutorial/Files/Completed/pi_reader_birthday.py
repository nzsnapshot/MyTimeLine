filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

#
# birthday = input('Enter your birthday in this format DDMMYY:')
# if birthday in pi_string:
#     print('Your birthday appears in the first million digits of pie string')
# else:
#     print('Get good idiot')

