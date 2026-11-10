'''
Create a list containing five fruit names.
    1. Convert the list into an iterator using iter().
    2. Use next() to display the first three fruits.
    3. Display the remaining fruits using a for loop.
'''

fruits = ["Apple", "Banana", "Mango", "Papaya", "Orange"];
fruits_iterator = iter(fruits);
print(next(fruits_iterator));
print(next(fruits_iterator));
print(next(fruits_iterator));

for fruit in fruits_iterator:
    print(fruit);