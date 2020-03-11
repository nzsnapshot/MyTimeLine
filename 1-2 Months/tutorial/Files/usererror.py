while True:

    try:
        number1 = int(input("Please enter the first number you would like to add: "))
        number2 = int(input("Please enter the first number you would like to add: "))

        answer = print(number1 + number2)
    except ValueError:
        print("Please enter a number not a letter you stoopid fuck")