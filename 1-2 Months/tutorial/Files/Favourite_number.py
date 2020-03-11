import json

def check_fornumb():
    """File name"""
    filename = 'fav_number.json'
    try:
        with open(filename) as f:
           number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def fav_numb():
    filename = 'fav_number.json'
    try:
        number = int(input('Please enter your favourite number'))

        with open(filename, 'w') as f:
            json.dump(number, f)
    except ValueError:
        return None
    else:
        return number

def print_numb():
    number = check_fornumb()
    if number:
        print(f"I know what your favourite number is: {number}")
    else:
        number = fav_numb()
        print(number)

check_fornumb()
print_numb()



