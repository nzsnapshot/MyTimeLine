filename = 'guest_book'

while True:
    name = input('What is your name? ')
    if name.lower() == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
            print(f"{name.title()} you have been added to the guest book")
