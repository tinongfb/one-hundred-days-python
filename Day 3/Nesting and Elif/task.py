while True:
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height > 120:
        print("You can ride the rollercoaster!")
        age = input("How old are you?")
        if age.isdigit():
            age = int(age)
            if age < 12:
                print("Pay $5")
            elif age >= 12 and age < 18:
                print("Pay $7")
            else:
                print("Pay $12.")
    else:
        print("Sorry you have to be taller to ride the rollercoaster.")

