'''
    Find the largest number.

    Create a lambda function that accepts two numbers and returns the largest number.

    Example: largest(25, 40) should return 40.
'''

largest = lambda num1, num2 : num1 if num1 > num2 else num2;
print(largest(30,20));