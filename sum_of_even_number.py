initial_value = 0;
number = 0;
run_times = 0;

while(True):
    entered_number = int(input("Enter a Number: "));
    if(entered_number == 0):
        print("You entered Zero, Please enter the number!");
    elif(entered_number < 0):
        print("You Entered negative value, Please Enter the positive number!");
    else:
        number = entered_number;
        break;

run_times = int(number/2);
sum = 0;

for x in range(run_times):
    initial_value = initial_value + 2;
    sum = sum + initial_value;
    print(initial_value);

print("Addition is: ",sum);