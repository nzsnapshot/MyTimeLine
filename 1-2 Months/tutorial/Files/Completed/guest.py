filename = 'guest.txt'

with open(filename, 'w') as f:
    guest_name = input('Please enter your name:')
    f.write(guest_name)