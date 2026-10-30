import random;

is_running = True;
random_number = random.randint(1,10);
attempts = 0;

while(is_running):
    attempts = attempts + 1;
    user_entered_number = int(input("Enter a Number: "));
    if(random_number < user_entered_number):
        print("Too High!");
    elif(random_number > user_entered_number):
        print("To Low!")
    else:
        print("Correct! You guessed it in",attempts,"attempts.");
        break;
