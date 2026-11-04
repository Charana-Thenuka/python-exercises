# Normally, a function accepts a fixed number of arguments.
# But what if you want to add 3, 5, or even 10 numbers?
# You would need to change the function every time.
# This is where *args becomes useful.

def add_numbers(*args):
    total = 0;

    for number in args:
        total += number;

    return total;

sum = add_numbers(10,20);
sum1 = add_numbers(20,30,40);
print(sum);
print(sum1);
