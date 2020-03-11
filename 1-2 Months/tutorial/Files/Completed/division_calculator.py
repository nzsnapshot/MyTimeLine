print("\nGive me two numbers to divide")
print("Enter 'q' to quit")

while True:
    number1 = input('\nFirst Number: ')

    if number1 == 'q':
        break
    number2 = input('Second Number: ')
    if number2 == 'q':
        break
    try:
        answer = int(number1) / int(number2)
    except ZeroDivisionError:
        print('Are you STOOPID')
    else:
        print(answer)
