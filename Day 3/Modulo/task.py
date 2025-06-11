while True:
    number = input("Enter a number: ")
    if number.isdigit():
        actual_number = int(number)
        answer = actual_number % 2
        if answer != 0:
            print("Number is not even."),
        else:
            print("Number is even.")
    else:
        pass
