correct_pin = "1020";
balance = 10000;
attempts = 0;
not_authenticate = True;
is_authenticate = False;

# Check the Balance
def check_balance():
    print("Your Balance is: ", balance);

# Deposit Function
def deposit_amount():
    deposit = 0;
    global balance;
    deposit_amount = int(input("Enter Deposit Amount: "));
    deposit = deposit + deposit_amount;
    balance = balance + deposit;
    return deposit;

# Withdraw Function
def withdraw_amount():
    withdraw_amount = int(input("Enter the Withdraw Amount: "));
    if(withdraw_amount > balance):
        print("Insufficient Amount, your account balance is Low!");
    else:
        print("Successfully Withdraw the Rs,",withdraw_amount, "Your new account Balance is Rs.",(balance-withdraw_amount))

# Only 3 attemps
for x in range(3):
    entered_pin = input("Enter the PIN: ");

    if(correct_pin == entered_pin):
        print("Authenticate Success!");
        print();
        is_authenticate = True;
        break;
    
    if(x == 2):
        print("You Reached your all 3 attempts!");
    else:
        print("Incorrect PIN, Enter Again!");

while(is_authenticate):
    print("===== ATM =====");
    print("1. Check Balance");
    print("2. Deposit");
    print("3. Withdraw");
    print("4. Exit");

    # new line
    print();

    option = input("Enter the number (1-4): ")

    match (option):
        case "1":
            check_balance();
            print();
        case "2":
            deposit = deposit_amount();
            print("Rs,",deposit, "Successfully Deposit, Your new balance is Rs,", (balance));
            print()
        case "3":
            withdraw_amount();
            print()
        case "4":
            print("Successfully Exit from the ATM!");
            is_authenticate = False;
            print();
        case _:
            print("Invalid Option, Please select (1-4) option!");
            print();