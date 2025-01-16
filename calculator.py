def get_number(prompt):
    """Prompts the user for a number and returns it as a float."""
    while True:
        # Keep asking for input until a valid number is provided
        try:
            return float(input(prompt))
        except ValueError:
            # If the input cannot be converted to float, inform the user
            print("Please enter a valid number.")

def calculate(num1, num2, operator):
    """Performs calculation based on the operator provided."""
    # Addition operation
    if operator == "+":
        return num1 + num2
    # Subtraction operation
    elif operator == "-":
        return num1 - num2
    # Multiplication operation
    elif operator == "*":
        return num1 * num2
    # Division operation
    elif operator == "/":
        # Check for division by zero to prevent runtime error
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    # If the operator is not one of the above, return an error message
    else:
        return "Invalid operator"

def main():
    loop = True
    while loop:
        # Prompt the user for the operator they wish to use
        operator = input("Enter an operator (+ - * /): ")
        if operator in ("+", "-", "*", "/"):
            # Get the first number from the user
            num1 = get_number("Enter the 1st number: ")
            # Get the second number from the user
            num2 = get_number("Enter the 2nd number: ")
            
            # Perform the calculation with the given numbers and operator
            result = calculate(num1, num2, operator)
            
            # If result is a string, it's an error message
            if isinstance(result, str):  
                print(result)
            else:
                # Print the result rounded to three decimal places
                print(f"Result: {round(result, 3)}")
            
            # Ask if the user wants to perform another calculation
            choice = input("Would you wish to continue? (yes/no): ").lower()
            # Exit the loop if the answer is anything but 'yes'
            if choice != "yes":
                loop = False
        else:
            # Inform the user if they've entered an invalid operator
            print(f"{operator} is not a valid operator")

if __name__ == "__main__":
    # Standard Python idiom to call the main() function when this script is run directly
    main()