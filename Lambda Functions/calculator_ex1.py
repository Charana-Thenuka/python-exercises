'''
    Create a simple calculator using lambda functions.

    Create four lambda functions:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    Each function should accept two numbers.
'''

# addition
add = lambda num1, num2 : num1+num2;
print(add(10,20));

# Substraction
sub = lambda num1, num2 : num1 - num2;
print(sub(50,20));

# Multiplication
multy = lambda num1, num2 : num1*num2;
print(multy(10,20));

# Division
div = lambda num1, num2 : num1/num2;
print(div(50,2));