filename = 'poll.txt'

while True:
    print('\nEnter "quit" at any stage to stop the poll\n')
    polls = input('Tell us why you love programming: ')
    if polls == 'quit':
        break
    else:
        confirm = input(f"You have entered:\n\n{polls}\n\nType confirm if this is correct ")
        with open(filename, 'a') as f:
            if confirm.lower() == 'confirm':
                f.write(f"{polls}\n")


