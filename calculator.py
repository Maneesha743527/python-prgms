def simple_calculator():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation_choice = input("Enter your operation choice (1-4): ")

    if operation_choice == '1':
        result = number1 + number2
        print(f"The result of addition is: {result}")
    elif operation_choice == '2':
        result = number1 - number2
        print(f"The result of subtraction is: {result}")
    elif operation_choice == '3':
        result = number1 * number2
        print(f"The result of multiplication is: {result}")
    elif operation_choice == '4':
        if number2 != 0:
            result = number1 / number2
            print(f"The result of division is: {result}")
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operation choice.")

simple_calculator()


