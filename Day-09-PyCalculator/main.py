from art_calculator import logo


# Basic arithmetic functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary mapping symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    # Display calculator logo
    print(logo)

    # Get first number
    num1 = float(input("What's the first number?: "))

    # Show available operations
    for symbol in operations:
        print(symbol)

    # Get operation and second number
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))

    # Execute selected operation
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(n1=num1, n2=num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    should_continue = True
    while should_continue:
        # Ask user what to do next
        continue_answer = input(
            f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new"
            f" calculation, or type 'e' to exit.: "
        ).lower()

        if continue_answer == 'y':
            # Continue with previous result
            operation_symbol = input("Pick an operation: ")
            next_num = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            final_answer = calculation_function(n1=first_answer, n2=next_num)

            print(f"{first_answer} {operation_symbol} {next_num} = {final_answer}")

            # Update result for next loop
            first_answer = final_answer

        elif continue_answer == 'n':
            # Restart calculator (recursion)
            return calculator()
        else:
            # Exit loop
            should_continue = False


# Start the program
calculator()
