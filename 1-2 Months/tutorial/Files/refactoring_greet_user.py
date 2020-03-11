import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username2.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    correct_user = input(f"Before we log you in, is this the correct login '{username}' ( Yes or No ): ")
    if correct_user == 'yes':
        print(f"Welcome back {username}")
    elif correct_user == 'no':
       get_new_username()
       new_user = get_new_username()
       print(f"Welcome back {new_user}")
    else:
        print('Fucked up')

greet_user()