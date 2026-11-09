'''
    What is map()?

    - The map() function applies another function to every item in an iterable, such as a list.

    Understanding the syntax

    - map(function, iterable)
        function: The operation you want to perform.
        iterable: The collection of values you want to process.
'''

# normal way
numbers = [1, 2, 3, 4, 5];
squre = [];

for number in numbers:
    squre.append(number ** 2);

print(squre);

# using lambda and map
new_numbers = [6,7,8,9,10];
squres = list(map(lambda x : x**2, new_numbers));
print(squres);

# Convert names to uppercase - Normal Way
names = ["kamal", "nimal", "amal"];
names_caps = []
for name in names:
    names_caps.append(name.upper());

print("Old", names_caps);

# using lambda and map()
names_caps_new = list(map(lambda name : name.upper(), names));
print("New", names_caps_new);