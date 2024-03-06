# Program to run inside while loop
run = True

while run == True:

    # Take the first numbers from the user
    number_1 = input("please enter the first value:")

    # Check to see if the value given is a number
    try: 
        number_1 = int(number_1)

    # If it isn't, ask again, and specify a number
    except:
        while number_1.isnumeric() == False:
            number_1 = input("Value must be a number, please enter the first value:")
          

    # Take the second number from the user
    number_2 = input("please enter the second value:")

    # Check to see if the value given is a number
    try:
        number_2 = int(number_2)
    
    # If it isn't, ask again, and specify a number
    except:
        while number_2.isnumeric() == False:
            number_2 = input("Value must be a number, please enter the second value:")
    
    # Have the user select an option 
    print("Which operation do you wish to perform:")
    print("1. Multiplication")
    print("2. Division")
    print("3. Addition")
    print("4. Subtraction")
    print("5. Modulo")
    print("6. Quit")
    choice = input("Please select an option:")

    # Perform chosen opteration (also covert strings to intergers)
    if choice == "1":
        answer = number_1*number_2
    elif choice == "2":
        answer = number_1/number_2
    elif choice == "3":
        answer = number_1+number_2
    elif choice == "4":
        answer = number_1-number_2
    elif choice == "5":
        answer = number_1%number_2
    else:
        # Alow user to exit the program
        run=False

    # Output answer
    print(answer)
