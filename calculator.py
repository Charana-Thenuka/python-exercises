is_running = True;

# Addition Function
def addition():
    number1 = int(input("Enter first number:"));
    number2 = int(input("Enter second number:"));

    return number1 + number2;

# Subtraction Function
def subtraction():
    number1 = int(input("Enter first number:"));
    number2 = int(input("Enter second number:"));

    return number1 - number2;

# Multiplication Function
def multiplication():
    number1 = int(input("Enter first number:"));
    number2 = int(input("Enter second number:"));

    return number1*number2;

# Division Function
def division():
    number1 = int(input("Enter first number:"));
    number2 = int(input("Enter second number:"));

    if(number2 == 0):
        print("Cannot divide by zero.");
    else:
        print("Division is: ", number1/number2);


while(is_running):
    print("===== Calculator =====");
    print("1. Addition");
    print("2. Subtraction");
    print("3. Multiplication");
    print("4. Division");
    print("5. Exit");

    option = input("Enter the Operation Number (1-5): ");

    match (option):
        case "1":
            # Addition Calculation
            print("addition is: ", addition());
        case "2":
            # Subtraction Calculation
            print("Subtraction is: ", subtraction());
        case "3":
            # Multiplication Calculation
            print("Multiplication is: ", multiplication());
        case "4":
            # Division Calculation
            division();
        case "5":
            # Exit
            print("===== Exit =====")
            break;
        case _:
            print("Enter correct number (1-5): ")
            