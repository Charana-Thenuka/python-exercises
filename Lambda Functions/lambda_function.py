'''
    1. What is a Lambda Function?
        A lambda function is a small, anonymous function that can be written in a single line.
'''

# normal function to calculate the squre
def squre(number):
    squre_number = number*number;
    return squre_number;

squre_number = squre(4);
print("Squre is: ", squre_number);

# using lambda function
squre = lambda number: number*number
print(squre(9));

'''
2. Understanding Lambda Syntax

lambda arguments: expression

    Part	            Meaning
    lambda	            Keyword used to create a lambda function
    arguments	        Values passed into the function
    :	                Separates arguments from the expression
    expression	        Operation whose result is returned
'''

# Find the largest number
largest = lambda a,b : a if a > b else b;
print("Largest Value: ",largest(30,20));

# Check whether a number is even
even_number = lambda a : a % 2 == 0
print(even_number(10));
print(even_number(9));