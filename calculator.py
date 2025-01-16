loop = True # Loop for the code - True means Active

while loop: # Start of the loop
    operator = input("Enter an operator ( + - * /): ") # Asks for user input of an operator

    if operator in ("+","-","*","/"): # If operator has been selected in the list, the user will be prompted to be a specific calculation
        num1 = float(input("Enter the 1st number: ")) # Saves data to variable num1 and ensures it's float
        num2 = float(input("Enter the 2nd number: ")) # Saves data to variable num2 and ensures it's float

        if operator == "+": # If user chosen an + operation, this section of the code will execute.
            result = num1 + num2 # adds num1 and num2 values and saves it in the result variable
            print(round(result, 3)) # outputs the added numbers and rounds it to 3 decimal places.
            choice = input(("Would you wish to continue?: ")).lower() # User can select to do more operations or close the program (NOTES: it's saved as an lowercase)
            if choice == "no": #If answer is no then the loop will end and the program will stop.
                loop = False # End of the loop.
        elif operator == "-": # Same applies as the previous code
            result = num1 - num2
            print(round(result, 3))
            choice = input(("Would you wish to continue?: ")).lower()
            if choice == "no":
                 loop = False
        elif operator == "*":
            result = num1 * num2
            print(round(result, 3))
            choice = input(("Would you wish to continue?: ")).lower()
            if choice == "no":
                 loop = False
        elif operator == "/":
            result = num1 / num2
            print(round(result, 3))
            choice = input(("Would you wish to continue?: ")).lower()
            if choice == "no":
                 loop = False

    else:
            print(f"{operator} is not a valid operator") # If user selects an input which is not from the list, program will not let it execute.
