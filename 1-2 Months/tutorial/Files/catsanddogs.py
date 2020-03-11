def cats_and_dogs(filename, filename2):

    """Used to enter 3 cats and dogs name"""

    print('\nEnter "quit" to quit at anytime.\n')

    while True:
        cats = input('Please enter your cats name: ')
        # Quit if quit is entered in the cat input
        if cats.lower() == 'quit':
            break
        dogs = input('Please enter your dogs name: ')
        # Quit if quit is entered in the dog input
        if dogs.lower() == 'quit':
            break
        else:
            # This is wrapped in a {try - Except} statement if it gives back any errors to do with File not found
            try:
                # Cat - If there is no file, it will create a file and add to that file with append function
                with open(filename, 'a') as c:
                    c.write(f'{cats.title()}\n')
                    print(f"\n{cats.title()} Has been added to our list")
                # Dog - If there is no file, it will create a fie and add to that file with append function.
                with open(filename2, 'a') as d:
                    d.write(f'{dogs.title()}\n')
                    print(f"{dogs.title()} Has been added to our list\n")
            except FileNotFoundError:
                print('File was not found G')


filename1 = 'cats2.txt'
filename2 = 'dogs.txt'
cats_and_dogs(filename1, filename2)
