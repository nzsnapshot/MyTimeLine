filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(f"{pi_string[:52]}....")
print(len(pi_string))

