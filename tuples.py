#  A tuple is a collection of items, just like a list.
#  The main difference is that a tuple cannot be changed after it is created. We call this immutable.

# When should you use tuples?
# Use tuples when you have data that should not change.

# List
fruits = ["Apple", "Banana", "Orange"];
fruits[0] = "Papaya";
print(fruits);

# Tuple
names = ("Amal", "Lakmal", "Nimal");
print(names);

# we can store multiple data types inside the tuple
student = ("Kamal", 25, 85.5);
print(student);

# access tuple elements
print(student[0]);

# Tuple methods - count()
numbers = (10, 20, 10, 30, 10);
print(numbers.count(10));

# index()
fruits = ("Apple", "Banana", "Orange");
print(fruits.index("Apple"));
