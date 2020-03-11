import json

# Load username, if it has been stored previously,
# Otherwise, prompt for the username and store it.
filename = 'username2.txt'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename,'w') as f:
        json.dump(username, f)
        print(f"We'll remember your {username} for your return!")
else:
    print(f"Welcome back! {username}")