import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)