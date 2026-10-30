correct_password = "python123";

for x in range(3):
    entered_password = input("Enter password:");

    if(correct_password == entered_password):
        print("Login successful!");
        break;
    elif(x == 2):
        print("Account locked!");
    else:
        print("Wrong password!");