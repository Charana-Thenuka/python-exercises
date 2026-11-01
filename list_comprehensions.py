# List comprehension is a shorter way to create a new list from an existing sequence, such as a list
# or a range.

# Normal way
numbers = [];

for x in range(1,6):
    numbers.append(x);

print(numbers);

# Using List Comprehension
numbers_using_list_comprehension = [x for x in range(1,6)];
print(numbers_using_list_comprehension);

# Print squre numbers (1-5)
squre_numbers = [x*x for x in range(1,6)]
print(squre_numbers);

# Even numbers between (1-11) - normal way
even_numbers = [];
for x in range(1,11):
    if(x % 2 == 0):
        even_numbers.append(x);

print(even_numbers);

# Even numbers between (1-11) - Using List Comprehension
even_numbers_using_list_comprehension = [x for x in range(1,11) if x % 2 == 0];
print(even_numbers_using_list_comprehension); 

# convert string to uppercase - Using List Comprehension
names = ["kamal", "nimal", "amal"];
uppercase_name = [name.upper() for name in names];
print(uppercase_name);
