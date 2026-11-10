numbers = [10, 20, 30, 40];

# Normally iterate the list through loop
for number in numbers:
    print(number);

# using iterarors
my_iteraror = iter(numbers);

print(next(my_iteraror));
print(next(my_iteraror));
print(next(my_iteraror));
print(next(my_iteraror));

fruits = ["Apple", "Banana", "Orange"]

fruit_iterator = iter(fruits);
print(next(fruit_iterator));
print(next(fruit_iterator));

