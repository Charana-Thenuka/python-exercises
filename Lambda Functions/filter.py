'''
What is filter()?
    - The filter() function selects items from a collection based on a condition.

Syntax:
    filter(function, iterable)

    - function: A condition that returns True or False.
    - iterable: The collection you want to check.
'''

# Find even numbers
numbers = [10, 15, 20, 25, 30, 35];
even_numbers = [];

for number in numbers:
    if(number % 2 == 0):
        even_numbers.append(number);

print(even_numbers);

# using filter and lambda functions
new_even_numbers = list(filter(lambda number : number % 2 == 0, numbers));
print("New ", new_even_numbers);

# Filter students who passed
marks = [35, 75, 45, 90, 60, 25];
passed_Students = list(filter(lambda mark : mark >= 50, marks));
print(passed_Students);


